use std::fs;
use std::io::{BufRead, BufReader, Read};
use std::path::Path;
use sha2::{Sha256, Digest};
use hex;

/// Valida integridade de um arquivo contra hash SHA256
fn validar_arquivo(caminho: &str, hash_esperado: &str) -> Result<bool, String> {
    let arquivo = fs::File::open(caminho)
        .map_err(|e| format!("Erro ao abrir {}: {}", caminho, e))?;

    let mut hasher = Sha256::new();
    let mut reader = BufReader::new(arquivo);
    let mut buffer = [0; 8192];

    loop {
        match reader.read(&mut buffer) {
            Ok(0) => break,
            Ok(n) => {
                hasher.update(&buffer[..n]);
            }
            Err(e) => return Err(format!("Erro ao ler {}: {}", caminho, e)),
        }
    }

    let resultado = hasher.finalize();
    let hash_calculado = hex::encode(resultado);

    Ok(hash_calculado.eq_ignore_ascii_case(hash_esperado))
}

/// Carrega e valida arquivo de manifesto (formato: "hash arquivo")
fn validar_manifesto(manifesto_path: &str) -> Result<(), String> {
    let arquivo = fs::File::open(manifesto_path)
        .map_err(|e| format!("Erro ao abrir manifesto {}: {}", manifesto_path, e))?;

    let reader = BufReader::new(arquivo);
    let base_dir = Path::new(manifesto_path)
        .parent()
        .unwrap_or(Path::new("."));

    let mut linhas_total = 0;
    let mut linhas_ok = 0;
    let mut falhas = Vec::new();

    for (num_linha, linha) in reader.lines().enumerate() {
        let linha = linha.map_err(|e| format!("Erro ao ler linha {}: {}", num_linha + 1, e))?;
        let linha = linha.trim();

        // Ignora linhas vazias e comentários
        if linha.is_empty() || linha.starts_with('#') {
            continue;
        }

        linhas_total += 1;

        // Parse: "hash  arquivo"
        let partes: Vec<&str> = linha.split_whitespace().collect();
        if partes.len() != 2 {
            falhas.push(format!("Linha {}: formato inválido (esperava 'hash arquivo')", num_linha + 1));
            continue;
        }

        let hash_esperado = partes[0];
        let arquivo_nome = partes[1];

        let caminho_completo = base_dir.join(arquivo_nome);
        let caminho_str = caminho_completo.to_string_lossy().to_string();

        match validar_arquivo(&caminho_str, hash_esperado) {
            Ok(true) => {
                linhas_ok += 1;
                println!("✓ {}", arquivo_nome);
            }
            Ok(false) => {
                falhas.push(format!("✗ {}: hash NÃO confere", arquivo_nome));
            }
            Err(e) => {
                falhas.push(format!("✗ {}: {}", arquivo_nome, e));
            }
        }
    }

    // Resultado final
    println!("\n{}", "=".repeat(60));
    println!("VALIDAÇÃO DE MANIFESTO");
    println!("{}", "=".repeat(60));
    println!("Total de arquivos: {}", linhas_total);
    println!("OK: {}", linhas_ok);
    println!("FALHAS: {}", falhas.len());

    if !falhas.is_empty() {
        println!("\nDetalhes das falhas:");
        for falha in &falhas {
            println!("  {}", falha);
        }
        println!("{}", "=".repeat(60));
        return Err(format!("Manifesto NÃO validado: {} falhas encontradas", falhas.len()));
    }

    println!("Status: ✓ VALIDADO (100% dos arquivos OK)");
    println!("{}", "=".repeat(60));
    Ok(())
}

fn main() {
    use std::env;
    use std::io::Read;

    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Validador de Manifesto SHA256 - Biblioteca Constantinopla-Alexandria v0.1");
        println!();
        println!("Uso:");
        println!("  {} <manifesto.sha256>", args[0]);
        println!();
        println!("Formato do manifesto:");
        println!("  <hash_sha256>  <arquivo>");
        println!("  <hash_sha256>  <arquivo>");
        println!();
        println!("Exemplo:");
        println!("  a1b2c3d4e5f6...  catalogo/pilar-1-vida-abundante.md");
        println!("  f6e5d4c3b2a1...  permanencia.md");
        println!();
        println!("Comentários (começam com #) são ignorados.");
        std::process::exit(1);
    }

    let manifesto_path = &args[1];

    match validar_manifesto(manifesto_path) {
        Ok(_) => std::process::exit(0),
        Err(e) => {
            eprintln!("ERRO: {}", e);
            std::process::exit(1);
        }
    }
}
