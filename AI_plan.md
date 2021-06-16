AI plan

Most basic version of bot is based on many if statements. We want to move away from this and introduce a scoring system for the AI:s to maximise.
Every condition is checked for every move and the conditions are independent.

We are concidering to score board positions instead of moves.

Points          Event
200             Victory, capture a stone
-100            Defeat, suicide a stone
5               Atari a stone
-20             Leave a stone in atari
3X              Reduce number of own groups by connecting them solidly. More points are rewarded, when connected groups had less liberties.
2X              Reduce liberties of liberties of an opposing group. More points are rewarded, when group has less liberties.
X               Add liberties for own groups. More points are rewarded, when group has less liberties.
-5              Put stone in corner
-2              Put stone in edge
  
