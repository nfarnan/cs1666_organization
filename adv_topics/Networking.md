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
- Client-Server Architecture (15 minutes)
  - The roles of the client and server: sending inputs, deciding game state, and displaying results.
  - How inputs reach the server and updated states return to both clients.
  - Why the server updates gameplay at a fixed tick rate.
  - What we've implemented: synchronized movement and basic attacks; what's next: respawns and screen transitions.

- What's Next — Advanced Networking (30 minutes)
  - Screen Synchronization: The server controls screen transitions and player spawns.
  - Client-Side Prediction: Show local movement before the server responds.
  - Interpolation: Smooth remote movement between server updates.
  - Server-Side Rewind: Account for latency when validating attacks and parries.
