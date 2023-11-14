# AI Advanced Topic Presentations

Before your presentation, use this file to get your talk outline approved. Be
sure to provide an estimated time to spend on teach topic (totalling 45 minutes)
and be sure not to repeat any topics covered in previous presentations.

## Presentation I

Vansh Desai 
Mary Grady
Jon Riklan

Outline


Summary from README: 

“Enemy AI will mainly focus on the implementation of the boss fight. Using utility AI, we will assign a point system that will calculate the systematically most efficient move that the enemy should make at any given instance when in combat with the player. Based on this point system, the enemy will decide its actions that will prove most dire for the player. This should make the boss fight extremely difficult for the player to beat without thinking like the enemy. In addition, we will track the player's combat decisions throughout the game. We can measure the average time the player takes between attacks, as well as its movement, to allow the enemy to know the most efficient time to attack and block the player. For smaller enemies, we will have a basic AI that follows the player around from point A to point B while making its basic default assigned attacks. Finally, the number of smaller enemies will be dependent on the number of active players. We will have N+1 smaller enemies in any given dungeon, where N is the number of active players. Four behaviors for boss include attack, block, avoid, and change target.”

Introduction: 

-	Intro to advanced topic (generalized to be specified later)
-	Explanation of final boss fight i.e. a short description of player vs enemy from the start of the game to the final boss fight
-	Basically and overview of what we are trying/will be accomplishing before we break it down into specifics 
-	Introduction to Utility AI : focus not so much on the use of AI (as in this is an upper level course so we don’t need to go into that much detail)  
-	Why is this AI useful for this situation 
-	Specifics relating to utility vs opposing ones 
-	Utility AI is a decision making system that allows the system to gather data on the current situation and allow the NPC to make a coordinated action in that exact moment 
-	The action with the highest score will win
-	Consideration: scores probability of something in this case players choice vs boss then decision 
-	Condition: allows a true of false 
-	Score mapping: job to map one or more scores into other single score 
-	How will utility AI work in this game? 
-	Mention specifics relating to player decisions and how this is the main deciding factor for the main boss 
-	Mention point system, go into depth later.


Sub-topic 1: Tracking player movement – point system (utility AI) (14 minutes)

-	In depth explanation of point system and how we are going to assign certain player movement to boss level integration of said movement. (i.e. how will these points dictate how the boss moves) 
-	How will points be assigned to players based on movement
-	How each movement is scored
-	How boss will use this score to know which movement is which and decipher how to counter it 
-	Movement capabilities of boss integrated into AI 



Sub-topic 2: Choices – point system (utility AI) (14 minutes)

-	In depth explanation of point system and how we are going to assign certain player decisions to boss level integration of said decisions.
-	How will points be assigned to specific actions 
-	Players have these possible actions: attack, dash
-	The point system needs to specify 1-10 point system
-	Which assignment goes to which task/ decision 
-	Movement, decision of player? 
-	Boss decision and movement 
-	However we are choosing to formulate or change these scores/points into actions for reasonable choice by the boss
-	Level of priority 
-	Point system is predetermined, but we calculate expected utility of an action and then compare it to our point system that we decided for actions
-	Changes during boss fight or no 
-	Difficulty modifier than can be applied depending on the level of enemy (i.e. small boss, medium boss, main boss)
-	This can be used to multiply by the utility that is calculated from our general scale


Sub-topic 3: Possible player actions vs possible boss actions (utility AI)  (14 minutes)

-	Boss is given the ability for four separate behaviors: attack, block, avoid, and change target.
-	How will the point system affect these choices?
-	As explained about the point system is designed to track the player’s decisions and movement and assigns a score to said player–these are specific to each player 
-	Based on calculated probabilities of possible responses to the players actions using the expected utility formula, in combination with the utility of different boss actions, the proper action will be taken at the time of player response
-	In terms of score – what will said score impose in terms of boss fight
-	If score is this do this etc….


Sub-topic 4: Smaller bosses (simplified AI) (14 minutes)

-	Intro to how the smaller enemies are worked into the game/ ie their role and why we used a basic AI for them vs the main boss 
-	Algorithm of tracking player position 
-	How it is implemented and possible collisions avoided 
-	How the smaller enemies play into the “block” and “avoid” points since smaller enemies only attack 


## Presentation II
- Hybrid Behaviour Tree: Overview, Design, and Implementation
  - Hybrid as in it is utility based combined with some event driven aspects 
- Sub-Topic 1: Behaviour Tree Overview (15 Minutes)
  - FSMs -> decision trees + planning algorithms + hierarchical structures -> behavior tree
    - Different Type of Behaviour Tree Nodes 
  - Types of behavior trees
    - How does it differs in behaviour selections
  - Specific applications of behavior trees
    - Video game AI, NLP, Robotics, etc.
- Sub-Topic 2: Behaviour Tree Implementation and Design Philosophy in Existing Games (15 Minutes)
  - Take a look at how games like Halo 2 and Spores designed their AI behaviour trees
  - The Intention -> Decision -> Action Tree structure
  - Impulse Behaviours
    - Event Driven Behaviour
    - Dynamic modification on the tree mid-execution 
  - Implementation Constraints
    - Execution speed
    - Memory constraints from the data structure
- Sub-Topic 3: Behaviour Tree Implemntation in Cats with Bats (15 Minutes)
  - NPC States
    - Intention States and how it build into selecting actions
   - How NPC difficulty affects the probability of an NPC being in a particular state
    - Decision Selection Probability
    - Formula of Probability Calculation
  - How behaviors are implemented within states
    - A* algorithm for pathfinding when moving towards and away from the ball
    - Some event driven impulse selections
  - Walkthrough of an example action being executed

## Presentation III
- Poker AI and the CFR algorithm for texas hold em'
  - The development of poker AI history and then delve into the two AIs we've implemented
- Brief History of Poker AI (5 minutes)
  - The evolution of AI specifically for Texas Hold Em'
  - Different Models and varying levels of success
- Our Easy AI with an example (10 minutes)
  - The inception and basics of our Easy AI algorithm
    - Simple random decisions based on a hand strength score
  - Basic example of how our Algorithm might score and act in a hand
- Introduce Regret Matching with another exmaple of RPS (10 minutes)
  - Regret matching and how it is a simple strategy in game theory that allows you to reach a nash equilibrium
  - An example of a couple rounds of Rock Paper Scissors to show how it would slowly shift regrets
- CFR as an application of Regret Matching and How we use it in our Texas Hold Em' Game (20 minutes)
  - CFR and the game theory behind it as an algorithm
  - The slight alterations between CFR and our own implementation
  - 1 or 2 hand example to show how the regrets are updated at each decision node and how this might lead to the application of training the AI before hand rather than starting at even odds everytime
...
