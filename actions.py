# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
# from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


# from excel_data_store_read import DataStore


class SalaryForm(FormAction):

    def name(self):
        return "form_info"

    @staticmethod
    def required_slots(tracker):
        return ["workplace", "min_salary", "fair_salary", "max_salary", "wish_salary"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "workplace": [
                self.from_entity(entity="workplace"),
            ],
            "min_salary": [
                self.from_entity(entity="salary"),
            ],
            "fair_salary": [
                self.from_entity(entity="salary"),
            ],
            "max_salary": [
                self.from_entity(entity="salary"),
            ],
            "wish_salary": [
                self.from_entity(entity="salary"),
            ],
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Danke für Mitmachen!")
        return []

# class ActionSaveData(Action):
#     def name(self) -> Text:
#         return "action_save_data"  # name of the form
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         DataStore(tracker.get_slot("softskills"),
#                   tracker.get_slot("workplace"))
#                   # tracker.get_slot("min_salary"),
#                   # tracker.get_slot("fair_salary"),
#                   # tracker.get_slot("max_salary"),
#                   # tracker.get_slot("wish_salary"))
#         dispatcher.utter_message(text="Data Stored successfully!")

#
# class FormDataCollect(FormAction):
#     def name(self):
#         return "form_info"  # name of the form
#
#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         return ["softskills", "workplace", "min_salary", "fair_salary", "max_salary",
#                 "wish_salary"]
#
#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         """A dictionary to map required slots to
#        #             - an extracted entity
#        #             - intent: value pairs
#        #             - a whole message
#        #             or a list of them, where a first match will be picked"""
#         return {
#             "softskills": [self.from_text(intent="inform")],
#             "workplace": [self.from_text(intent="inform")],
#             "min_salary": [
#                 self.from_text(intent="inform"),
#             ],
#             "fair_salary": [
#                 self.from_text(intent="inform"),
#             ],
#             "max_salary": [
#                 self.from_text(intent="inform"),
#             ],
#             "wish_salary": [
#                 self.from_text(intent="inform"),
#             ],
#         }
#
#     def submit(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         dispatcher.utter_message("Danke für Mitmachen!")
#         return []
#
#     # def submit(
#     #         self,
#     #         dispatcher: "CollectingDispatcher",
#     #         tracker: "Tracker",
#     #         domain: Dict[Text, Any],
#     # ) -> List[EventType]:
#     #     dispatcher.utter_message("Danke für Mitmachen!")
#     #     return []
