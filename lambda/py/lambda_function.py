# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from data.french import language
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = language.LAUNCH
        handler_input.attributes_manager.session_attributes["previousIntent"] = "launchRequest"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class YesHandler(AbstractRequestHandler):
    """If the user says Yes, they want another fact."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        session_attr = handler_input.attributes_manager.session_attributes
 
        # Get the slot value from the request and add it to the session 
        # attributes dictionary. Because of the dialog model and dialog 
        # delegation, this code only ever runs when the favoriteColor slot 
        # contains a value, so a null check is not necessary.
        previous_intent = session_attr.get("previousIntent")
        logger.info("In YesHandler")
        logger.info(f"previous intent was: {previous_intent}")
        if previous_intent == "launchRequest":
            handler_input.attributes_manager.session_attributes["previousIntent"] = "YesHandler"
            return IntroductionRequestHandler().handle(handler_input)
        if previous_intent == "IntroductionRequest":
            handler_input.attributes_manager.session_attributes["previousIntent"] = "YesHandler"
            return FavoriteLocationRequestHandler().handle(handler_input)

class NoHandler(AbstractRequestHandler):
    """If the user says No, then the skill should be exited."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In NoHandler")
        handler_input.attributes_manager.session_attributes["previousIntent"] = "NoHandler"
        return handler_input.response_builder.speak(language.GOODBYE).set_should_end_session(True).response

class IntroductionRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        session_attr = handler_input.attributes_manager.session_attributes
        previous_intent = session_attr.get("previousIntent")

        if previous_intent == "launchRequest":
            return True
        return False

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = language.INTRODUCTION_PROPOSITION
        handler_input.attributes_manager.session_attributes["previousIntent"] = "IntroductionRequest"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FavoriteLocationRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_request_type("FavoriteLocationRequestHandler")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = language.FAVORITE_LOCATION
        handler_input.attributes_manager.session_attributes["previousIntent"] = "FavoriteLocationRequest"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class NatureChoiceRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        session_attr = handler_input.attributes_manager.session_attributes
        previous_intent = session_attr.get("previousIntent")

        if previous_intent == "FavoriteLocationRequest":
            return True
        return ask_utils.is_request_type("NatureChoiceRequestHandler")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = language.NATURE_CHOICE_PROPOSITION
        handler_input.attributes_manager.session_attributes["previousIntent"] = "NatureChoiceRequest"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class StareAtNatureRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return (ask_utils.is_request_type("StareAtNatureRequest")(handler_input) or
                ask_utils.is_intent_name("StareAtNatureIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = language.STARE_AT_NATURE_PROPOSITION
        handler_input.attributes_manager.session_attributes["previousIntent"] = "StareAtNatureRequestHandler"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_should_end_session(True)
                .response
        )

class FeelTheNatureRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return (ask_utils.is_request_type("FeelTheNatureRequest")(handler_input) or
                ask_utils.is_intent_name("FeelTheNatureIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = language.FEEL_THE_NATURE_PROPOSITION
        handler_input.attributes_manager.session_attributes["previousIntent"] = "FeelTheNatureRequestHandler"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_should_end_session(True)
                .response
        )

class DeepDiveIntoNatureRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return (ask_utils.is_request_type("DeepDiveIntoNatureRequest")(handler_input) or
                ask_utils.is_intent_name("DeepDiveIntoNatureIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = language.DEEP_DIVE_INTO_NATURE_PROPOSITION
        handler_input.attributes_manager.session_attributes["previousIntent"] = "DeepDiveIntoNatureRequestHandler"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_should_end_session(True)
                .response
        )

class LearnAboutNatureRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return (ask_utils.is_request_type("LearnAboutNatureRequest")(handler_input) or
                ask_utils.is_intent_name("LearnAboutNatureIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = language.LEARN_ABOUT_NATURE_PROPOSITION
        handler_input.attributes_manager.session_attributes["previousIntent"] = "LearnAboutNatureRequestHandler"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_should_end_session(True)
                .response
        )

class ParticipativeScienceNatureRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return (ask_utils.is_request_type("ParticipativeScienceNatureRequest")(handler_input) or
                ask_utils.is_intent_name("ParticipativeScienceNatureIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = language.PARTICIPATIVE_SCIENCE_NATURE_PROPOSITION
        handler_input.attributes_manager.session_attributes["previousIntent"] = "ParticipativeScienceNatureRequestHandler"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_should_end_session(True)
                .response
        )
class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response

class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

sb = SkillBuilder()

sb.add_request_handler(YesHandler())
sb.add_request_handler(NoHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(NatureChoiceRequestHandler())
sb.add_request_handler(IntroductionRequestHandler())
sb.add_request_handler(StareAtNatureRequestHandler())
sb.add_request_handler(FeelTheNatureRequestHandler())
sb.add_request_handler(DeepDiveIntoNatureRequestHandler())
sb.add_request_handler(LearnAboutNatureRequestHandler())
sb.add_request_handler(ParticipativeScienceNatureRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
