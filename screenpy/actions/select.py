from selenium.webdriver.support.ui import Select as SelSelect

from ..pacing import beat, MINOR


class Select(object):
    """
    Selects an option from a dropdown menu. This is a superclass that will
    create the correct specific Select action that will need to be used,
    depending on how the option needs to be selected. Some examples of
    invocations:

        Select.the_option_named("January").from_the(MONTH_DROPDOWN)
        Select.the_option_at_index(0).from_the(MONTH_DROPDOWN)
        Select.the_option_with_value("jan").from_the(MONTH_DROPDOWN)

    It can then be passed along to the :class:`|Actor|` to perform the
    action.
    """

    @staticmethod
    def the_option_named(text: str) -> "SelectByText":
        """
        Instantiate a :class:`|SelectByText|` class which will select the
        option with the given text.

        Args:
            text (str): The text of the option to select.

        Returns:
            :class:`|SelectByText|`
        """
        return SelectByText(text)

    @staticmethod
    def the_opton_at_index(index: int) -> "SelectByIndex":
        """
        Instantiate a :class:`|SelectByIndex|` class which will select the
        option at the specified index. This index is 0-based.

        Args:
            index (int): The index (0-based) of the option to select.

        Returns:
            :class:`|SelectByIndex|`
        """
        return SelectByIndex(index)

    @staticmethod
    def the_option_with_value(value: str) -> "SelectByValue":
        """
        Instantiate a :class:`|SelectByText|` class which will select the
        option with the given text.

        Args:
            value (str): The text of the option to select.

        Returns:
            :class:`|SelectByText|`
        """
        return SelectByValue(value)


class SelectByText(object):
    """
    A specialized Select action that chooses the option by text. This
    class is meant to be accessed via the Select action's static
    :meth:`|Select|.the_option_with_text` method. A typical invocation
    might look like:

        Select.the_option_named("January").from_the(MONTH_DROPDOWN)

    It can then be passed along to the :class:`|Actor|` to perform the
    action.
    """

    def from_the(self, target: "Target") -> "SelectByText":
        """
        Provides the :class:`|Target|` to select the option from.

        Args:
            target (Target): The :class:`|Target|` describing the dropdown
                element to select from

        Returns:
            :class:`|SelectByText|`
        """
        self.target = target
        return self

    def from_(self, target: "Target") -> "SelectByText":
        """Syntactic sugar for :meth:`|SelectByText|.from_the`."""
        self.target = target
        return self

    @beat("{0} selects the option '{text}' from the {target}.", gravitas=MINOR)
    def perform_as(self, the_actor: "Actor") -> None:
        """
        Asks the actor to attempt to find the dropdown element described
        by the stored target, then performs the select action.

        Args:
            the_actor (Actor): The :class:`|Actor|` who will perform the
                action.

        Raises:
            :class:`|Actor|.UnableToPerformException|: if the actor does
                not have the ability to :class:`|BrowseTheWeb|`.
        """
        element = self.target.resolve_for(the_actor)
        select = SelSelect(element)
        select.select_by_visible_text(self.text)

    def __init__(self, text: str) -> None:
        self.text = text


class SelectByIndex(object):
    """
    A specialized Select action that chooses the option by its index. This
    class is meant to be accessed via the Select action's static
    :meth:`|Select|.the_option_at_index` method. A typical invocation
    might look like:

        Select.the_option_at_index(0).from_the(MONTH_DROPDOWN)

    It can then be passed along to the :class:`|Actor|` to perform the
    action.
    """

    def from_the(self, target: "Target") -> "SelectByIndex":
        """
        Provides the :class:`|Target|` to select the option from.

        Args:
            target (Target): The :class:`|Target|` describing the dropdown
                element to select from

        Returns:
            :class:`|SelectByIndex|`
        """
        self.target = target
        return self

    def from_(self, target: "Target") -> "SelectByIndex":
        """Syntactic sugar for :meth:`|SelectByIndex|.from_the`."""
        self.target = target
        return self

    @beat("{0} selects the option at index {index} from the {target}.", gravitas=MINOR)
    def perform_as(self, the_actor: "Actor") -> None:
        """
        Asks the actor to attempt to find the dropdown element described
        by the stored target, then performs the select action.

        Args:
            the_actor (Actor): The :class:`|Actor|` who will perform the
                action.

        Raises:
            :class:`|Actor|.UnableToPerformException|: if the actor does
                not have the ability to :class:`|BrowseTheWeb|`.
        """
        element = self.target.resolve_for(the_actor)
        select = SelSelect(element)
        select.select_by_index(self.index)

    def __init__(self, index: int) -> None:
        self.index = index


class SelectByValue(object):
    """
    A specialized Select action that chooses the option by its value. This
    class is meant to be accessed via the Select action's static
    :meth:`|Select|.the_option_with_value` method. A typical invocation
    might look like:

        Select.the_option_with_value("jan").from_the(MONTH_DROPDOWN)

    It can then be passed along to the :class:`|Actor|` to perform the
    action.
    """

    def from_the(self, target: "Target") -> "SelectByValue":
        """
        Provides the :class:`|Target|` to select the option from.

        Args:
            target (Target): The :class:`|Target|` describing the dropdown
                element to select from

        Returns:
            :class:`|SelectByValue|`
        """
        self.target = target
        return self

    def from_(self, target: "Target") -> "SelectByValue":
        """Syntactic sugar for :meth:`|SelectByValue|.from_the`."""
        self.target = target
        return self

    @beat(
        "{0} selects the option with value '{value}' from the {target}.", gravitas=MINOR
    )
    def perform_as(self, the_actor: "Actor") -> None:
        """
        Asks the actor to attempt to find the dropdown element described
        by the stored target, then performs the select action.

        Args:
            the_actor (Actor): The :class:`|Actor|` who will perform the
                action.

        Raises:
            :class:`|Actor|.UnableToPerformException|: if the actor does
                not have the ability to :class:`|BrowseTheWeb|`.
        """
        element = self.target.resolve_for(the_actor)
        select = SelSelect(element)
        select.select_by_value(self.value)

    def __init__(self, value: str) -> None:
        self.value = value