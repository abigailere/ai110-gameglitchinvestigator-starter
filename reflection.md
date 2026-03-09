# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The game allowed you to guess numbers until you find the secret number and the range of numbers depended on the difficulty. Some of the bugs were obvious as soon as you start it but others took more work to find. One obvious bug was that when you guessed a number was lower than the answer, the hint would tell you to go lower instead of higher. Also, the game allowed guesses that were supposed to be out of range. Anothee bug was that the game could not restart once you've failed.
    
    
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude extension because it was already in vscode so it could see all my code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  One of the problems I identified was that the ranges of allowed values changing with each difficulty, the game was not applying that rule when picking a secret number. Claude suggested changing the random range that was originally 1 to 100 to instead be between the low and high variables which fixed the issues. I tested this restarting the game for each difficulty several times and checking what the secret number was. I also guessed numbers that were out of range, and the game no longer allowed that. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  When trying to fix the ranges, Claude changed the range for easy mode from 1-20 to 1-22. I found this when I was testing the ranges for generating the secret number. I read the "thinking" drop down to see what logic it was running through when it made that change and then prompted it to fix it and clarified my intentions.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
  I tested my code by running the running the game and inputting values that I knew were supposed to be wrong and would have been allowed before the fix. For example, I guessed numbers that were out of range to see if that guess would be accepted. For testing the new game bug, I toggled between the difficulties to check that there were different secret numbers being generated and I clicked the button several times to also check. I didn't use AI to help me generate new tests but I used it to help me understand the tests that were already written so I could understand what it meant when it failed or passed.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
  The secret kept changing because when the button was clicked the entire script would run, which was a problem for the random generator because it would be called after every run. 
  I saved the secret number in a session state so it would stay consistant in reruns and generated a new number only if it was not already in session state that way, once its called and created the statement is false and it would generate another one. 
  A session state kinda works like a save button. If you are typing in a word doc and click save, what you typed will stay there even if you refresh the document. Without a way to save, everytime you refresh, the document would forget it and be blank. This is like how Streamlit works without session states. Streamlit is like the doc, session states like the save button, and a rerun like hitting refresh. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  After a few suggestions, I found it easier to understand the changes the AI made if I had it comment out the old code and briefly explain the change there. This made it easier for me to check because I could see the old and new code next to eachother as well as check if the generated code was consistant with what the AI said it would do. This project made me even more aware of how the way I prompt AI can also affect the code it generates. Being too vague can lead it in the wrong direction. In the future I will set out rules for Claude to follow before I start the session so its suggestions are consistant. I think that would make it easier for me to verify its work.
