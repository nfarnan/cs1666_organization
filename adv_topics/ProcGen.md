# Procedural Generation Advanced Topic Presentations

Before your presentation, use this file to get your talk outline approved. Be
sure to provide an estimated time to spend on teach topic (totalling 45 minutes)
and be sure not to repeat any topics covered in previous presentations.

## Presentation I - Untitled Squirrel Group

- Procedural Generation Overview (10 minutes)
  - What is procedural generation?
  - What is it used for?
  - How is it used in video games specifically?
  - What are the benefits of using procedural generation?
  - What are the disadvantages of using procedural generation?
- Binary Space Partitioning (10 minutes)
  - What is binary space partitioning?
  - How is BSP implemented? More specifically, how can it be implemented for platforming games?
  - BSP trees
  - Visual representation of BSP that we can walk the class through for better understanding
  - Applications of binary space partitioning
- Random Walk Algorithm (10 minutes)
  - What is the random walk algorithm?
  - How is random walk implemented for procedural cave generation?
  - Visual representation of random walk that we can walk the class through for better understanding.
  - Applications of random walk
- Feature placement (10 min)
  - What do we mean by feature placement?
  - Difficulties surrounding feature placement in procedural generation
  - The different kinds of features to consider and challenges they bring
  - Potential approaches and their advantages/disadvantages
- Finding a balance (5 minutes)
  - How can a balance be struck between procedural generation and hand-created maps/levels within a game?


## Presentation II - Red Delicious

- Introduction (5 minutes)
  - Provide examples of how the Perlin Noise algorithm is used in real-world contexts
  - Discuss how Perlin Noise is used to generate terrain, texture, world-building
- Understanding Perlin Noise (25 minutes)
  - What is Perlin Noise?
  - Perlin Noise properties
  - How does Perlin Noise work?
  - Combining and Layering Noise
  - Perlin Noise Implementation in our 2D Game
  - How we tweaked the Perlin Noise algorithm
  - Procedural Generation Demo
  - Perlin Noise Variants
- Challenges and Future Plans (10 minutes)
  - Limitations and Challenges
  - Future Plans
    - Blue Noise
    - Texture Generation
    - Graphs
- Conclusion (5 minutes)
    - Summarize critical takeaways from the presentation
    - Reinforce the importance of Perlin Noise in creating natural-looking patterns


## Presentation III

- Introduction (5 minutes)
  - Subteam introduction
  - Broad overview of the scale of the map of our game
  - Introduction of navigable vs. non-navigable room generations to introduce the problem we’re trying to solve
- Depth First Search Overview (15 minutes)
  - What is Depth First Search (DFS)?
  - Using DFS to verify the existence of a path between 2 nodes in a graph (step through)
  - What does DFS look like on a 2D array of 0’s and 1’s (step through)?
- DFS In Our Game (10 minutes)
  - Overview of the entity types used to represent the tiles in our game
  - What if the grid has more than 2 possible values?
    - is_passable() recursive function walkthrough (the DFS function in our game)
  - What if a floor is not navigable?
- Challenges and Conclusion (5 minutes)
  - Discuss rooms in our game that are more complex than moving from Point A to Point B (puzzle rooms and combat rooms).
  - Summarize main points and wrap up DFS discussion.

