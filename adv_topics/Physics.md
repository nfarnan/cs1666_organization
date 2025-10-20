# Physics Advanced Topic Presentations

Before your presentation, use this file to get your talk outline approved. Be
sure to provide an estimated time to spend on teach topic (totalling 45 minutes)
and be sure not to repeat any topics covered in previous presentations.

## Presentation 1
### TEAM1_NAME

1. What we are implementing in terms of physics (2-3 mins)
    a. Fluid dynamics
          - How air particles interact with each other and their surroundings
          - How air particles react to a vacuum created
    b. How is it going to be impacting the gameplay (1-2 minutes)
          - Enemies, player’s, and objects will all be subjected to the same physics simulation
          - They will all be pulled towards the low pressure area where a breach has occurred
          - After the oxygen levels reach a certain level, the player will no longer be able to breath and will get a game over if they do not leave 
            the level fast enough
    c. Why is this an advanced topic (1-2 minutes)
           - Requires advanced calculations each frame to determine where the air particles will be and interact with each other
           - Complex interactions with objects, players, enemies
2. History of implementing fluid dynamics 
    a. Early approximations (1980s–1990s) (2-3 minutes)
          - animated textures or particles.
          - Super Mario 64 example
    b. Physics-based effects (2-3 minutes)
          - Navier–Stokes–based solvers
          - simplified smoothed-particle hydrodynamics and height-field water models.
    c. Why other algorithms required improvement
         - Navier–Stokes Solvers (2-3 minutes)
                  1. Computationally very expensive
                  2. unstable without damping
          - Smoothed Particle Hydrodynamics (2-3 minutes)
                  1. Poor at simulating continuous surfaces like smoke
                  2. frame rate drops
          - Procedural Noise (2- 3minutes)
                  1. Not physically accurate
                  2. Good for visuals
          - Lattice Gas Automata (2-3 minutes)
                  1. Hard to get smooth, stable fluid motion
     d. LBM Goal 
           - improve upon LGA by averaging out random noise and representing fluid motion more smoothly
      e. Noise perlin
3. LBM 
    a. History (2-3 minutes)
          - Based off of LGA (Lattice Gas Automata)
          - LBM created because people desired to remove statistical noise and get a smoother representation of fluid behavior
    b. Author of the algorithm (1 min)
          - (1988-1989)McNamara, Zanetti, Higuera, Succi, Benzi
    c. Other uses (2 mins)
          - Aerospace and cars
          - Liquid flow through pipes
          - Biomedical uses: blood flow, airflow in lungs
            - Realistic fluids in games and movies
    d. High concept overview (5 - 10 minutes)
          - Discretization of space / velocity
          - The two main steps each time step
                1. Streaming
                2. Collision
          - Calculation of density and velocity
     e. Advantages (2-3 minutes)
          - Very good for GPUs as many of the calculations can be done in parallel
          - Handles complex boundaries easily
          - Straightforward to implement
      f. Disadvantages (2 mins)
            - Scaling it to large real-world sizes can require very fine grids, which is computationally expensive
            - Comparatively high memory usage to other CFD solvers
                      1. This gets worse the more accurate you want the simulation to be
            -  Cannot handle compressible flow
      g. Inputs and outputs (graphs)
      h. Talk about methods individually(slide per important method 2-4 minutes per method 5 methods combined)
       i. Sources
              - Lattice Boltzmann methods - Wikipedia (https://en.wikipedia.org/wiki/Lattice_Boltzmann_methods#:~:text=The%20main%20motivation%20for%20the,so%2Dcalled%20density%20distribution%20function.)
              - Navier–Stokes–based solvers (https://www.sciencedirect.com/science/article/abs/pii/S004578252100058X)
               - Smoothed-particle hydrodynamics (https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics)
                - Lattice Gas Automata (https://www.sciencedirect.com/science/article/pii/S0167739X9900045X)
                - Lattice Gas Automata2 (https://en.wikipedia.org/wiki/Lattice_gas_automaton)
      j. Potential demo

