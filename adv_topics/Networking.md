# Networking Advanced Topic Presentations

Before your presentation, use this file to get your talk outline approved. Be sure to provide an estimated time to spend on teach topic (totalling 45 minutes) and be sure not to repeat any topics covered in previous presentations.


## Presentation 1
### Tower Balance (Danny, Sam, Polly)
- What we've done so far (10 minutes)
  - Setting up a UDP server.
  - How the host listens for a player
  - How the client connects to host
  - Error checking port
- Server Authoritative Model (10 minutes)
  - Peer to Peer vs Server Authoritative
  - Seperating client and server code
- Client Side Prediction (15 minutes) 
- Latency and Tick Rate (15 minutes)
  - Game running at set tick amount (using fixed update)
  - Sending data from client to server and vice versa
  - Rollback


## Presentation 2
### Team1 (Superkill) (Eric, Brian, Chen)
- What We've Done So Far — Tokio, UDP, Serde, and Postcard (15 minutes)
  - How Tokio enables asynchronous multiplayer networking using UDP.
  - How the server listens for connections and assigns player IDs.
  - How Serde serializes Rust structs and Postcard converts them into bytes for transmission.
  - How clients and servers exchange messages (Connect, PlayerInput, GameState).
- Client-Server Architecture (15 minutes)
  - Separating client, server, and shared networking code.
  - How inputs travel from clients to the server and updated states return.
  - Our current implementation: synchronizing player movement.
- What's Next — Advanced Networking (20 minutes)
  - Screen Synchronization: Server controls screen transitions and player spawns.
  - Client-Side Prediction: Move locally without waiting for server responses.
  - Interpolation: Smooth remote player movement between server updates.
  - Server-Side Rewind: Account for latency when validating attacks and parries.
 

