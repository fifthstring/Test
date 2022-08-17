#alpha complex
1
'''
Alpha Complex consists of many connected rooms. Each room is identified by a single (unique) letter
and each exit from a room is marked with the letter identifying the room to which it is connected.
A spy is moving systematically through Alpha Complex. For each room they keep track of whether they
have visited it an even or an odd number of times. They also record, for each room and for each exit,
whether they have left the room through that exit an odd or even number of times.
The spy moves between rooms according to the following rules:
• If they have visited the room an odd number of times, they will leave through the exit which is
marked with the first letter alphabetically;
• If they have visited the room an even number of times, they will find the first exit alphabetically that
they have left through an odd number of times. If that is the last exit alphabetically in this room
they will leave through it, otherwise they will leave through the next exit alphabetically.
When the spy starts exploring Alpha Complex, they have visited their starting room an odd number of
times (i.e. once), each other room an even number of times (i.e. zero) and have left through each exit an
even number of times (i.e. zero).
For example, suppose that they start in room X, which has exits to B, I and O:
• They have visited X an odd number of times, so they leave the room through the first exit
alphabetically, which is B;
• When they are next in X they will have visited it an even number of times. The first exit
alphabetically that they have left through an odd number of times is B. As this is not the last exit
alphabetically, they leave through exit I;
• Subsequent visits to the room will see them leave through B, O, B, I, B, O, ...
Alpha Complex consists of r (r ≥ 3) rooms, identified by the first r letters of the alphabet. The spy is in
possession of a secret plan, giving the connections between the rooms. This plan is an ordered list of r-2
letters and the spy can construct a map of the complex as follows:
• The spy will choose the first room alphabetically which has not yet been chosen and which is not in
the plan. The chosen room is connected to the first room in the plan. The first room is then
removed from the plan;
• The above step is repeated until the plan is empty;
• There will be two rooms which have not yet been chosen. These two rooms are connected together.
If two rooms are connected, each room has an exit to the other room.
'''

c = [[]]