##AGB deny
* greet
    - utter_greet
* deny
    - utter_goodbye

## survey happy path
* greet
    - utter_greet
* affirm
    - utter_choose_group
* mint_student OR gender_female OR first_generation OR migration_background OR control_group
    - utter_ask_enroll_survey
* affirm
    - form_info
    - form{"name": "form_info"}
    - form{"name": null}
    - utter_slots_values
* thankyou OR affirm
    - utter_goodbye

    
## no survey
* greet
    - utter_greet
* affirm
    - utter_choose_group
* mint_student OR gender_female OR first_generation OR migration_background OR control_group
    - utter_ask_enroll_survey
* deny
    - utter_goodbye
    
## survey stop
* greet
    - utter_greet
* affirm
    - utter_choose_group
* mint_student OR gender_female OR first_generation OR migration_background OR control_group
    - utter_ask_enroll_survey
* affirm
    - form_info
    - form{"name": "form_info"}
* out_of_scope
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_goodbye   

## survey continue
* greet
    - utter_greet
* affirm
    - utter_choose_group
* mint_student OR gender_female OR first_generation OR migration_background OR control_group
    - utter_ask_enroll_survey
* affirm
    - form_info
    - form{"name": "form_info"}
* out_of_scope
    - utter_ask_continue
* affirm
    - form_info
    - form{"name": null}
    - utter_slots_values
    
