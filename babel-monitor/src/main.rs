use axum::{
    http::StatusCode,
    response::IntoResponse,
    routing::{get, post},
    Json, Router,
};
use serde::{Deserialize, Serialize};
use std::sync::Arc;
use tokio::sync::RwLock;
use tower_http::cors::CorsLayer;
use chrono::Utc;

#[derive(Clone, Serialize, Deserialize, Debug)]
struct GitHubMetrics {
    stars: u32,
    forks: u32,
    issues: u32,
    prs: u32,
    last_commit: String,
    commits_total: u32,
}

#[derive(Clone, Serialize, Deserialize, Debug)]
struct NetworkMetrics {
    github_clones: u32,
    ipfs_peers: u32,
    countries: Vec<String>,
    total_reach: u64,
}

#[derive(Clone, Serialize, Deserialize, Debug)]
struct LanguageMetrics {
    language: String,
    code: String,
    files: u32,
    completeness: f32,
}

#[derive(Clone, Serialize, Deserialize, Debug)]
struct DashboardData {
    timestamp: String,
    github: GitHubMetrics,
    network: NetworkMetrics,
    languages: Vec<LanguageMetrics>,
    status: String,
    growth_rate: f32,
}

struct AppState {
    data: Arc<RwLock<DashboardData>>,
}

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();

    let initial_data = DashboardData {
        timestamp: Utc::now().to_rfc3339(),
        github: GitHubMetrics {
            stars: 0,
            forks: 0,
            issues: 0,
            prs: 0,
            last_commit: "722fe8e".to_string(),
            commits_total: 40,
        },
        network: NetworkMetrics {
            github_clones: 0,
            ipfs_peers: 0,
            countries: vec!["BR".to_string(), "US".to_string()],
            total_reach: 1,
        },
        languages: vec![
            LanguageMetrics {
                language: "Português".to_string(),
                code: "pt".to_string(),
                files: 3,
                completeness: 1.0,
            },
            LanguageMetrics {
                language: "English".to_string(),
                code: "en".to_string(),
                files: 3,
                completeness: 1.0,
            },
            LanguageMetrics {
                language: "Español".to_string(),
                code: "es".to_string(),
                files: 3,
                completeness: 1.0,
            },
            LanguageMetrics {
                language: "中文".to_string(),
                code: "zh".to_string(),
                files: 3,
                completeness: 0.85,
            },
            LanguageMetrics {
                language: "हिन्दी".to_string(),
                code: "hi".to_string(),
                files: 3,
                completeness: 0.7,
            },
            LanguageMetrics {
                language: "العربية".to_string(),
                code: "ar".to_string(),
                files: 3,
                completeness: 0.7,
            },
            LanguageMetrics {
                language: "Русский".to_string(),
                code: "ru".to_string(),
                files: 3,
                completeness: 0.7,
            },
            LanguageMetrics {
                language: "日本語".to_string(),
                code: "ja".to_string(),
                files: 3,
                completeness: 0.7,
            },
        ],
        status: "🟢 OPERACIONAL".to_string(),
        growth_rate: 0.0,
    };

    let state = AppState {
        data: Arc::new(RwLock::new(initial_data)),
    };

    let app = Router::new()
        .route("/", get(dashboard_html))
        .route("/api/metrics", get(get_metrics))
        .route("/api/metrics/update", post(update_metrics))
        .route("/api/github", get(get_github_metrics))
        .route("/api/network", get(get_network_metrics))
        .route("/api/languages", get(get_languages))
        .layer(CorsLayer::permissive())
        .with_state(Arc::new(state));

    let listener = tokio::net::TcpListener::bind("127.0.0.1:3000")
        .await
        .unwrap();

    println!("🚀 BABEL Monitor iniciado em http://localhost:3000");
    println!("📊 Acesse em seu navegador para ver o dashboard em tempo real");

    axum::serve(listener, app).await.unwrap();
}

async fn dashboard_html() -> impl IntoResponse {
    (
        StatusCode::OK,
        [("Content-Type", "text/html; charset=utf-8")],
        include_str!("../static/index.html"),
    )
}

async fn get_metrics(
    axum::extract::State(state): axum::extract::State<Arc<AppState>>,
) -> impl IntoResponse {
    let data = state.data.read().await;
    Json(data.clone())
}

#[derive(Serialize, Deserialize)]
struct MetricsUpdate {
    github_stars: Option<u32>,
    github_forks: Option<u32>,
    github_issues: Option<u32>,
    github_prs: Option<u32>,
    ipfs_peers: Option<u32>,
    github_clones: Option<u32>,
    total_reach: Option<u64>,
}

async fn update_metrics(
    axum::extract::State(state): axum::extract::State<Arc<AppState>>,
    Json(update): Json<MetricsUpdate>,
) -> impl IntoResponse {
    let mut data = state.data.write().await;
    data.timestamp = Utc::now().to_rfc3339();

    if let Some(stars) = update.github_stars {
        data.github.stars = stars;
    }
    if let Some(forks) = update.github_forks {
        data.github.forks = forks;
    }
    if let Some(issues) = update.github_issues {
        data.github.issues = issues;
    }
    if let Some(prs) = update.github_prs {
        data.github.prs = prs;
    }
    if let Some(peers) = update.ipfs_peers {
        data.network.ipfs_peers = peers;
    }
    if let Some(clones) = update.github_clones {
        data.network.github_clones = clones;
    }
    if let Some(reach) = update.total_reach {
        data.network.total_reach = reach;
    }

    // Calcular taxa de crescimento (simplificado)
    data.growth_rate =
        ((data.github.stars as f32 + data.network.ipfs_peers as f32) / 100.0) * 10.0;

    Json(data.clone())
}

async fn get_github_metrics(
    axum::extract::State(state): axum::extract::State<Arc<AppState>>,
) -> impl IntoResponse {
    let data = state.data.read().await;
    Json(data.github.clone())
}

async fn get_network_metrics(
    axum::extract::State(state): axum::extract::State<Arc<AppState>>,
) -> impl IntoResponse {
    let data = state.data.read().await;
    Json(data.network.clone())
}

async fn get_languages(
    axum::extract::State(state): axum::extract::State<Arc<AppState>>,
) -> impl IntoResponse {
    let data = state.data.read().await;
    Json(data.languages.clone())
}
