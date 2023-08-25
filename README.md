NOTES/ Things to resolve/ figure out:
 1. algorithms suited for sequential data apart from the ones mentioned below?
 2. Can we treat this as a problem to predict next word or character in a sequence?
 3. Models to experiment with:
    a. Decision Trees
    b. HMM
    c. RNN
    d. Random Forest
    e. Ensemble methods
 4. Try to put weights on moves based on who won?
 5. We can treat the problem as sequence models like in NLP, probabilistic models like in HMM by using the list of only possible moves instead of all moves as the target variable  
 6. The corpus to choose moves from should change with every move. The new move should be the one with highest probability in that corpus.
 7. Is it possible to code how to evaluate a position?


 PLAN:

 1. Have a parser to get the moves from the PGN. Test with given data.
 2. Check if we can use the existing chess sdk to get legal moves in a position.
 3. Figure out how we can feed the moves ( PRESERVING THE ORDER ) to an algorithm and use who won that game to assign weights.
 4. How can we check the error in moves? Can we use the existing chess engine for it? Is there any sense to add an error? Figure out some way to calculate errors (maybe see if the move predicted is even legal at the least?). Can some existing error measure help here?
 5. Check if we can have custom errors calculated fed to the model.
 6. Split the data into train and test.
 7. Train the model.
 8. Test the model by playing a game against it.