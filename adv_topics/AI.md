# AI Advanced Topic Presentations

Before your presentation, use this file to get your talk outline approved. Be
sure to provide an estimated time to spend on teach topic (totalling 45 minutes)
and be sure not to repeat any topics covered in previous presentations.

## Presentation 1
67Studios
- Intro (2 minutes)
  - Clarify the definition of AI (not generative, but instead CPU players)
- History of CPUs in Video Games (10 minutes):
  - Early Chess implementations using trees
  - Pathing
    - Basic pathing - Duck Hunt
    - Okay Pathing - Legend of Zelda NES enemies
      - Targeting
      - Anti-link
    - Good Pathing - Pac-Man
    - Excellent Pathing - Mario Kart
  - We know how to construct a path, now how do we get the player there -> State Machines
- State Machines (XX minutes):
  - What state machines are formally / informally
  - Brief history of AI in video games
  - How state machines are used in the context of video game CPUs
    - Pac-Man state machine
    - State Machine flow charts (directed graphs), how to define behaviors and transitions between them
  - More advanced state machines
    - RTSes like Command and Conqueror, Starcraft
  - Artificial stupidity, “Cheating”
    - Mario Kart Slingshotting
    - Civilization
  - State transition tables, adjacency matrices
    - State machines within Unreal engine (for animations)
  - Example state machine implementations in pseudocode interspersed throughout

- Theta* is an Unusual Choice (XX minutes):
  - A* is Theta*’s older and more popular brother
    - Easier to implement and used commonly in the gaming industry
    - Results in more jagged movement
      - Used in conjunction with path smoothing algorithms
  - What is Theta*
    - Theta* is a pathfinding algorithm that can result in any-angle movement
    - Unlike A*, its paths are more natural and very smooth
    - It finds the shortest path, not the fastest path
  - Where is Theta* used?
    - Nowhere really. A single research paper mentions Maze Runner: Angel and Demon Path Finding Game Application which uses it.
    - Theta* is a huge pain to implement compared to A*
    - Much more complex than A* and path smoothing combined
  - Does it make sense for our game?
    - No
    - Theta* does NOT take velocity into account
      - ONLY cares about shortest path and obstacles
    - We should be using something called Waypoint Graphs + Pure Pursuit
    - Gold standard for this kind of game in the industry
- Different levels for AI Development
  - Using A* For path finding, changing around speed control or reaction time to vary bot levels
  - Change speed in which bots go around corners, for instance, or based on the angle in which they are turning
  - Challenges for altering different parts of A * for these purposes

## Presentation 2
### TEAM2_NAME

- Topic1 (XX minutes):
  - Subtopic1
  - Subtopic2
  - ...
- Topic2 (XX minutes):
  - Subtopic1
  - Subtopic2
  - ...
- Topic3 (XX minutes):
- ...
