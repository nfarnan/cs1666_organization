# AI Advanced Topic Presentations

Before your presentation, use this file to get your talk outline approved. Be
sure to provide an estimated time to spend on teach topic (totalling 45 minutes)
and be sure not to repeat any topics covered in previous presentations.

## Presentation 1
### 67Studios
- Intro (2 minutes)
  - Clarify the definition of AI (not generative, but instead CPU players)
- History of CPUs in Video Games (5 minutes):
  - Early Chess implementations using trees
  - Pathing
    - Basic pathing - Duck Hunt
    - Okay Pathing - Legend of Zelda NES enemies
      - Targeting
      - Anti-link
    - Good Pathing - Pac-Man
    - Excellent Pathing - Mario Kart
  - We know how to construct a path, now how do we get the player there -> State Machines
- State Machines (15 minutes):
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

- Theta* is an Unusual Choice (15 minutes):
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
- Different levels for AI Development (8 minutes):
  - Using A* For path finding, changing around speed control or reaction time to vary bot levels
  - Change speed in which bots go around corners, for instance, or based on the angle in which they are turning
  - Challenges for altering different parts of A * for these purposes

## Presentation 2
### Sherpa

- What is Q learning (15 minutes):
  - what is reinforcement learning (3 min)
    - the specifics of that goals
      - explotation versus explortation
      - what are rewards
  - what are actions and states within this framework (2 min)
    - Since state machines are foundational
      - what are the possible actions (jumping, left right, Jump L, jump R)
      - what are the possible states
        - these can be catagorized by cause and effect
  - what is a model free learning algorithm (3min)
    - model free
      - uses experiance without any foreknowlage 
        - without knowlage and expectations we instead store rewards
        - without an internal model of every cause and effects which means it doesn't simulate future actions
  - what is the Q learning algorithm (3min)
    - the current state and finding the most optimal transition
      - but the main caveat it does not guarante the choice of main optimal action
      - this chance of explore is reduced
    - modifying with the rewards 
      - we modify a table or some way to store which action was better given a reward

- what is our approach to developing the AI (15 minutes):
  - diagram of our approach to the algorithm in theory
    - the flow of information between game world and into the algorithm
  - traits 
    - what are traits and how do they interact with the game world
    - why is it from the game world into observer and why controller to game world
  - observer
    - The observer taking as an input of traits and what is the output of states
    - why do we need this observer and what does it determine about states
  - policy
    - what is the algorithm behind the policy and decision making itself
      - what does the starting q table look like and after a few rounds of training how does it change
      - when is it that we can stop explotation and start exploration 
  - controller
    - why is it returning traits 
- demonstration of what has been coded so far (10 minutes):
  - controller
    - show off code and what it does
  - states
    - show off code and what it does
  - policy
    - show off code and what it does
- what are the problems with Q learning and our own woes(5 min)
  - Q learning in a 2d platformer has many states
    - if everything interactable 
  - what problems were there in development 

