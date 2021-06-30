AI plan

Most basic version of bot is based on many if statements. We want to move away from this and introduce a scoring system for the AI:s to maximise.
Every condition is checked for every move and the conditions are independent.

We are considering to score board positions instead of moves.

Points          Event
200             Victory, enemy stone is captured (0 libs)
-100            Defeat, own stone is captured
20              Enemy stone is in atari. Points per capture threat
-50             Own stone is in atari
-3X             X is number of groups
-harmonicSum(n)
                n is liberties of an enemy group. Counted for each group individually.
harmonicSum(n)
                n is liberties of own group. Counted for each group individually.
-5 per stone    Own stone is in corner 
-2 per stone    Own stone is in edge
-0.5 per stone  Own stone on second line



evalAI1: Implement a rudimentary evaluation function (see above). Pick the move that results in the best evaluated position.