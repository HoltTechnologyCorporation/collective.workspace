from zope.component.interfaces import ObjectEvent


class TeamMemberEvent(ObjectEvent):
    """Base for team member events.

    This is used instead of normal Zope object lifecycle
    events so it can be dispatched based on the workspace
    rather than based on the modified object (which is
    just a dictionary in this case).
    """

    def __init__(self, object, memberdata):
        self.object = object
        self.memberdata = memberdata


class TeamMemberAddedEvent(TeamMemberEvent):
    """Event for when a member is added."""


class TeamMemberRemovedEvent(TeamMemberEvent):
    """Event for when a member is removed."""


class TeamMemberModifiedEvent(TeamMemberEvent):
    """Event for when a member is modified."""
