from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name, get_supported_interfaces
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model.interfaces.alexa.presentation.apl import RenderDocumentDirective

APL_DOCUMENT_ID = "reponseSkill"

APL_DOCUMENT_TOKEN = "documentToken"

DATASOURCE = {
    "textListData": {
        "type": "object",
        "objectId": "textListSample",
        "backgroundImage": {
            "contentDescription": null,
            "smallSourceUrl": null,
            "largeSourceUrl": null,
            "sources": [
                {
                    "url": "https://d2o906d8ln7ui1.cloudfront.net/images/templates_v3/textlist/AlexaTextListBackground_Dark.png",
                    "size": "large"
                }
            ]
        },
        "title": "Plant Stores Near Me",
        "listItems": [
            {
                "primaryText": "Peonies & Petals Nursery"
            },
            {
                "primaryText": "Ivy Lane Nursery and Tree Farm"
            },
            {
                "primaryText": "House of Hyacinth"
            },
            {
                "primaryText": "Swan Nursery"
            },
            {
                "primaryText": "House of Peonies"
            },
            {
                "primaryText": "Spruce Nursery"
            }
        ],
        "logoUrl": "https://d2o906d8ln7ui1.cloudfront.net/images/templates_v3/logo/logo-modern-botanical-white.png"
    }
}

class SampleAPLRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("INTENT_NAME")(handler_input)

    def supports_apl(self, handler_input):
        # Checks whether APL is supported by the User's device
        supported_interfaces = get_supported_interfaces(
            handler_input)
        return supported_interfaces.alexa_presentation_apl != None

    def launch_screen(self, handler_input):
        # Only add APL directive if User's device supports APL
        if self.supports_apl(handler_input):
            handler_input.response_builder.add_directive(
                RenderDocumentDirective(
                    token=APL_DOCUMENT_TOKEN,
                    document={
                        "type": "Link",
                        "src": f"doc://alexa/apl/documents/{APL_DOCUMENT_ID}"
                    },
                    datasources=DATASOURCE
                )
            )

    def handle(self, handler_input):
        # Add APL Template if device is compatible
        self.launch_screen(handler_input)
        # Generate JSON Response
        return handler_input.response_builder.response

sb = SkillBuilder()
sb.add_request_handler(SampleAPLRequestHandler())
lambda_handler = sb.lambda_handler()
© 2