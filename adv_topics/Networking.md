# Networking Advanced Topic Presentations

Before your presentation, use this file to get your talk outline approved. Be
sure to provide an estimated time to spend on teach topic (totalling 45 minutes)
and be sure not to repeat any topics covered in previous presentations.

## Presentation 1
### Sherpa

- Packet Frequency/Size Adjustments (5 mins):
  - How many packets per second should we send from the client 
  - How big/small should each packet be, and how frequently should/could they be sent?

  - ...
- Packet Loss, Congestion, and Out-of-Order Delivery (5 mins):
  - Reasons for packet loss
  - Patterns for packet dropping
  - When do messages start to come out of order?
  - Describe/simulate congestion

- How do you track time (2 mins):
  - Between two machines?
    - Keep it local
  - Time can be brittle
    - The system clock is not consistent between the two machines
  - Use Instants on one machine only.

- Ping and Jitter (3 mins):
  - How are ping and jitter measured, and what are the desired values of each for smooth gameplay?

- Frames vs Ticks (4 mins): 
  - Difference between visual frames vs the server tick rate
  - Tick rates' effect on consistency between players

- Client Side Prediction, Interpolation, Reconciliation (8 mins): 
  - Client-side predictions' role in hiding latency for the player
  - Running the server simulation offset by client RTT/2 for each client.
    - So the server will get snapshots from the player for the simulation at around the right moment.
    - The client plays the game now (predicts), and the server later confirms or corrects.
    - If the server is behind, how is the Local player getting the networked inputs at the time that the networked player sent them?
  - Interpolation
    - Smoothing between networked points
    - Must have packet timing data for good interpolation.
  - Reconciliation 
    - Rewind and replay your own recent inputs on top of the authoritative state.
  - Rubber banding.

- Determinism and Lockstep? (3 mins):
  - Define determinism and how issues here can lead to desyncs
  - What breaks determinism in an authoritative model?
  - Potential Demo of dropping packets and applying state after.
  - Because of UDP, we need to rollback on the server and apply late inputs.
  - Lockstep within multiplayer

- Server (4 mins):
  - Run the Bevy game code headless
    - Ensure game physics is deterministic 
    - In practice, this means to just seed any RNG.
  - Send and receive tasks created as Bevy IoTaskPool threads, that communicate with each other through channels.
  - Receiving input data (keys) + sending snapshots
  - Driving the simulation with networked key inputs
- Client (4 mins):
  - Sending keys, receiving snapshots
  - Has a receiving thread but not a send
  - Sending is done synchronously on each game frame at 60Hz.
- Adding lobby’s (3 mins):
  - Adding multiple lobbies would require creating multiple instances of the game simulation running in parallel. 
  - All of the traffic would be going through 1 UDP socket on the server
    - We should be able to handle handshakes + key inputs at the same time. And route the responses to the right client.
- AWS (2 mins):
  - Getting the server online is annoying, especially with UDP, because many places will block certain UDP traffic.
    - EC2 relay. 
    - TURN server provides a fallback (haven’t tried it)
  - Amazon GameLift (EC2 or containers)
    - Horizontal + Vertical scaling
    - Load Balancing


## Presentation 2
### Blueberry

- Design Philosophies for Networked Multiplayer (5 minutes):
  - "Don't Trust The Client"   
  - Limit Locally Stored Information
- Our Approaches to Following that Philosophy (5 minutes):
  - Packet Design
    - Client-to-Server
    - Server-to-Client
  - Authoritative Server
  	- Player Damage/Health 
- Planning for Network Conditions (25 minutes):
	- Synchronization
 		- Variable FixedUpdate	
	- Input History
  		- Compression
	- Rollback Methods
 		- Low Tech Overwrite
  		- Gradual Input Compression 
 	- Hit Registration
  		- Variable Bullet Size  	
- Worst Case Scenarios (10 minutes)
  - Ping
  - Packet Loss
  - Disconnects
  - Tradeoffs

## Presentation 3
### 67Studios

- Background: Codebase History (5 mins)
	- Peer to peer architecture (accident)
		- Difficult synchronizing lobby state with joins and (especially) leaves
	- Relay server that takes in client position
		- Bad design decision, trusting the client
	- Authoritative server (next section)
  
- Final Project Architecture (3 mins)
	- Diagram
		- Client-server architecture
		- Authoritative server
		- UDP
    
- Security and Firewalls (5 mins) 
	- Security concerns with accepting all network traffic onto a server
	- Firewalls
		- Problems firewalls caused for our project
		- Getting around firewalls issues
    
- Lobby (5 mins)
	- Quick run through of our actual lobby UI
	- Explain details of our lobby system with a state diagram of the lobby
		- What happens when you create a lobby
		- What happens when you join a lobby
		- What happens when you leave a lobby
		- Starting a lobby, which transitions into synchronized start
    
- Synchronized Start (5 mins)
	- Approaches
		- Start accepting traffic on server at specified time
			- Higher latency clients start behind
		- Client system clock based approach
			- Didn’t use because involves trusting client
	- What we landed on
		- Round trip ping latency approach
	- Some code snippets
	- Future improvements
   
- Introduce Lag Compensation (2 min)
	- Interpolation + Client-side prediction
   
- Interpolation (10 mins)
	- Review the problem of latency in networking
		- GIF/Video of our game being laggy pre-lag-compensation
		- Do not want remote players to be choppy
		- Explore potential solutions (interpolation, extrapolation, etc)
		- Land on interpolation, justify why for our game
	- Explain algorithm used (theory and equations)
		- Alternate algorithms for interpolation and why we chose our approach
	- Illustrative code snippets
	- Challenges we faced
	- Pre-recorded demo
		- Comparing network cars with vs without interpolation

- Client-Side Prediction (10 mins)
	- Review the problem
		- Do not want to rely on networking for our local player
		- Explore potential solutions
	- Explain our server reconciliation method
	- Smoother reconciliation methods
		- Incremental bending
	- Pre-recorded demo
		- Comparing local cars with vs without client-side prediction

