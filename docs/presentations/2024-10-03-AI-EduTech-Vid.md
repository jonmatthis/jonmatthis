# Questions about SkellyBot and AI EduTech

## 1 - How does SkellyBot differ from ChatGPT/GPT-4, etc
- Distinguishing MODEL (vs Agent) vs User Interface (UI)
  - 'Model' is the base tech
    - Think like "internal combustion engine"
  - 'Agent' is (roughly)Model+Tools
  - UI is the way we use it
    - Think like cars vs planes vs boats vs irrigation pumps
  
- SkellyBot currently represents a minimal UI onto `gpt4o` model, but that's very much not a constraint
  
- Briefly talk about how the basic ChatGPT/SkellyBot UI works (i.e. interface + server calls)
  - Mention that OpenAI is conflating 'agent' and 'model' with their latest `o1` models
  
- **KEY FACTORS OF CURRENT IMPLEMENTATION** 
  - Flexiblity and specificity of purpose
  - Heirarchical prompting frameworks
  - STUDENT CHAT DATA availability
  
## 2 - Integration with LMS (i.e. Canvas/Blackboard)?
- Yes, for sure! Could be built around the LMS' API for external applications 
  
## 3 - Long term development plans? 
- Discord definitely is NOT the long term plan! 
  - This is somewhere between 'proof of concept' and 'minimal viable product'
- Future is highly flexible, and can/will/must be built to suit specific use cases and adapted continuously based on real/desired user experiences

## 4 - Piloting solutions?
- Easiest route is to find some brave professors teaching 'topics' courses and adapt existing methods to their use cases
- Depending on desired timelines and available resources, we can do refactoring and development to improve various aspects of functionlity (i.e. refactor existing code, adapt to Slack, build bespoke UI, develop more robust processing/analysis pipelines, etc)