## Join path               <!-- name of the story - just for debugging -->
* greet              
  - utter_greet
* join               <!-- user utterance, in format _intent[entities] -->
  - utter_join
* thank_you
  - utter_goodbye

## About path               <!-- this is already the start of the next story -->
* greet
  - utter_greet             <!-- action of the bot to execute -->
* about
  - utter_about
* thank_you
  - utter_goodbye

## Upcoming path 
* greet
  - utter_greet
* upcoming
  - utter_upcoming
* thank_you
  - utter_goodbye
