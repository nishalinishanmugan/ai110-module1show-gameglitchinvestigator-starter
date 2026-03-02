# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
There were already issues when I started. The number we had to guess was 98. The hint kept saying lower. Until I guessed 1 when the range is from 1 to 100, and it still said to go lower. The game set-up looks fine in terms that the user can input a number, submit a guess, generate a new game, and toggle showing a hint or not. I think maybe the difficulty should also be a buttont instead of something on the left side?

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
Bug 1: The hint doesn't seem to be correct. It kept saying to guess lower and when I guessed 1, it continues to say lower when the correct number was supposed to be 98. The hint seems to print the opposite of the direction that the user should go. If the user should go lower, it tells the user to go higher and vice versa. 

Bug 2: When you click New Games, the pop-up text says "You already won the game.Start a new game to play". But I already clicked it. And it doesn't allow me to Submit another Guess. So I need to Reload the page. 

Bug 3: I don't think the difficulty level is correct. I think the hard level isn't harder compared to normal. 

I asked the AI to explain one of the bugs. And it pointed out that the logic was swapped for check_guess. If guess is greater than secret, it should tell the user to go lower instead of higher and vice versa. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude and ChatGPT for this project. I used Claude as an Extension on Visual Studio to ask specific questions about the code. And I used ChatGPT to ask specific questions about issues I was having running the code. For example, running pytest didn't work for me in the Test Driven Verification section because I was supposed to use py -m pytest instead.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested that the logic was swapped for check_guess. If the guess is greater than the secret, it should tell the user to go lower instead of higher, and vice versa. I thought about this logic and realized that it was correct. And then I fixed it and tested it to confirm that it was correct.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Well, one thing the AI said that was misleading was asking me to change update_score, but it didn't mention to delete some parts of the functions. So I fixed it, but kept the parts that were supposed to be deleted. And then I later figured it out. And when it came to fixing the Higher and Lower in check_guess, the AI didn't fix the emoji. It was show Higher with a lower graph emoji and as Lower with a higher graph emoji.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided that the bug was really fixed after I implemented the fix and then went back and reran the code. For example, I fixed the "GO HIGHER" and "GO LOWER" being swapped. When the guess was lower than the special number, it would say go lower instead of go higher and vice versa. So after I implemented the fix, I reran the code and checked make sure that the logic was correct now. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran the test_game_logic.py. I changed the tests to assert LOWER if the if the result are Too High and assert HIGHER if the results were Too Low. But this was also after I change the logic so the "GO LOWER" and "GO HIGHER" were now correct. So now after I ran py -m pytest, it showed that all the tests were now passing. 
- Did AI help you design or understand any tests? How?
The AI helped me understand or notice things that I didn't notice when I ran the program first myself. The AI helped me understand the st.session_state because I didn't initially understand it at first. I believe the AI helped me understand more bugs that I would have found without it. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Streamlit kept rerunning the entire script every time the user interacted with the app. So the secret number was being regenerated on every rerun. And that makes the game feel weird every time the user wants to start a new game.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time the user interacts with something on the app, like inputting a number to guess or pressing a button. Streamlit reruns the entire Python file. But it saves what you store in the st.session_state, so everything isn't gone every time you run. 
- What change did you make that finally gave the game a stable secret number?
The secret number was being stored inside st.session_state. It was only being generated if it didn't exist or if the difficulty level changed. The secret number is now only changed when the game starts, when the difficulty changes, or when the player selects a "New Game". 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I think a prompting strategy would be asking really specific questions about specific things I see to the AI instead of asking vague or generic things. 
- What is one thing you would do differently next time you work with AI on a coding task?
I would first look for issues in the code before asking questions to the AI, similar to the way we did with this project.  
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize that you need to ask really specific questions to AI to get the response you want. 

Challenge 5: AI Model Comparison
I asked ChatGPT and Claude AI about the "GO LOWER" and "GO HIGHER" but in the check_guess. And they both gave the same or similar responds in showing how to fix the issue. Claude was more clear and readable fix because I had the extension enabled and it could point it out directly in the code. But it didn't fix the emoji's just the text. But ChatGPT noticed that the text needed to be changed. 
