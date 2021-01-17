use serde::Deserialize;
use serde_bencode::de;
use std::env;

#[derive(Debug, Deserialize)]
struct Torrent {
    announce: String,
    info: Info,
}

#[derive(Debug, Deserialize)]
struct Info {
    name: String,

    length: u64,

    #[serde(rename="piece length")]
    piece_length: u64,

    // Binary blob of the hashes of all the pieces
    #[serde(with = "serde_bytes")]
    pieces: Vec<u8>,
}

fn parse_torrent_file(file: String) -> Result<Torrent, String> {
    // Read torrent file from disk
    let data = std::fs::read(file).map_err(|e| e.to_string())?;

    // Decode it (bencode)
    let torrent = de::from_bytes::<Torrent>(&data).unwrap();
    Ok(torrent)
}

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        println!("Expected one torrent file path as an argument");
        std::process::exit(1);
    }

    println!("Parsing torrent file: {}", args[1]);
    let torrent = parse_torrent_file(args[1].clone());
    println!("Decoded Torrent: {:?}", torrent);
}
