__all__ = [
    'BasePluginV1',
    'ImageAnnotationHotkeysPluginV1',
    'TextAnnotationHotkeysPluginV1',
    'HotkeysPluginV1',
    'TriggerPluginV1',
    'TolokaPluginV1',
]
import toloka.client.project.template_builder.base
import toloka.util._extendable_enum
import typing


class BasePluginV1(toloka.client.project.template_builder.base.BaseComponent, metaclass=toloka.client.project.template_builder.base.VersionedBaseComponentMetaclass):
    """Plugins that provide expanded functionality. For example, you can use plugin.hotkeys to set up shortcuts.
    """

    def __init__(self, *, version: typing.Optional[str] = '1.0.0') -> None:
        """Method generated by attrs for class BasePluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]


class ImageAnnotationHotkeysPluginV1(BasePluginV1):
    """Used to set hotkeys for the field.image-annotation component.

    You can set hotkeys to select area types and selection modes and to confirm or cancel area creation. When setting
    hotkeys, you can use the up and down arrows (up,down), numbers, and Latin letters.

    Attributes:
        cancel: Keyboard shortcut for canceling area creation.
        confirm: Keyboard shortcut for confirming area creation.
        labels: Keyboard shortcuts for choosing area types. They're assigned to buttons in the order they are shown if
            you enabled the option to choose multiple area types.
        modes: Keyboard shortcuts for choosing selection modes.
    """

    class Mode(toloka.client.project.template_builder.base.BaseTemplate):
        """Mode

        Attributes:
            point: Keyboard shortcut for selecting areas using points.
            polygon: Keyboard shortcut for selecting areas using polygons.
            rectangle: Keyboard shortcut for selecting areas using rectangles.
            select: Keyboard shortcut for selecting shapes and points.
        """

        def __init__(
            self,
            *,
            point: typing.Optional[str] = None,
            polygon: typing.Optional[str] = None,
            rectangle: typing.Optional[str] = None,
            select: typing.Optional[str] = None
        ) -> None:
            """Method generated by attrs for class ImageAnnotationHotkeysPluginV1.Mode.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        point: typing.Optional[str]
        polygon: typing.Optional[str]
        rectangle: typing.Optional[str]
        select: typing.Optional[str]

    @typing.overload
    def __init__(
        self,
        *,
        cancel: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        confirm: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]] = None,
        modes: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Mode]] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ImageAnnotationHotkeysPluginV1.
        """
        ...

    @typing.overload
    def __init__(
        self,
        *,
        cancel: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        confirm: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]] = None,
        point: typing.Optional[str] = None,
        polygon: typing.Optional[str] = None,
        rectangle: typing.Optional[str] = None,
        select: typing.Optional[str] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ImageAnnotationHotkeysPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    cancel: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
    confirm: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
    labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]]
    modes: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Mode]]


class TextAnnotationHotkeysPluginV1(BasePluginV1):
    """Use this to set keyboard shortcuts for the field.text-annotation component.

    Attributes:
        labels: Keyboard shortcuts for selecting categories. They're assigned to buttons with categories in the order
            they're shown.
        remove: Use this property to allow a Toloker to deselect an entire line or part of it. The key that you
            assign to this property will deselect.
    """

    def __init__(
        self,
        labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]] = None,
        remove: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TextAnnotationHotkeysPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]]
    remove: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]


class HotkeysPluginV1(BasePluginV1):
    """Lets you set keyboard shortcuts for actions.

    Attributes:
        key_ + [a-z|0-9|up|down]: An action that is triggered when you press the specified keyboard key. The keyboard
            shortcut is set in the key, and the action is specified in the value

    Example:
        How to create hotkeys for classification buttons.

        >>> hot_keys_plugin = tb.HotkeysPluginV1(
        >>>     key_1=tb.SetActionV1(tb.OutputData('result'), 'cat'),
        >>>     key_2=tb.SetActionV1(tb.OutputData('result'), 'dog'),
        >>>     key_3=tb.SetActionV1(tb.OutputData('result'), 'other'),
        >>> )
        ...
    """

    def __init__(
        self,
        *,
        key_a: typing.Optional[typing.Any] = None,
        key_b: typing.Optional[typing.Any] = None,
        key_c: typing.Optional[typing.Any] = None,
        key_d: typing.Optional[typing.Any] = None,
        key_e: typing.Optional[typing.Any] = None,
        key_f: typing.Optional[typing.Any] = None,
        key_g: typing.Optional[typing.Any] = None,
        key_h: typing.Optional[typing.Any] = None,
        key_i: typing.Optional[typing.Any] = None,
        key_j: typing.Optional[typing.Any] = None,
        key_k: typing.Optional[typing.Any] = None,
        key_l: typing.Optional[typing.Any] = None,
        key_m: typing.Optional[typing.Any] = None,
        key_n: typing.Optional[typing.Any] = None,
        key_o: typing.Optional[typing.Any] = None,
        key_p: typing.Optional[typing.Any] = None,
        key_q: typing.Optional[typing.Any] = None,
        key_r: typing.Optional[typing.Any] = None,
        key_s: typing.Optional[typing.Any] = None,
        key_t: typing.Optional[typing.Any] = None,
        key_u: typing.Optional[typing.Any] = None,
        key_v: typing.Optional[typing.Any] = None,
        key_w: typing.Optional[typing.Any] = None,
        key_x: typing.Optional[typing.Any] = None,
        key_y: typing.Optional[typing.Any] = None,
        key_z: typing.Optional[typing.Any] = None,
        key_0: typing.Optional[typing.Any] = None,
        key_1: typing.Optional[typing.Any] = None,
        key_2: typing.Optional[typing.Any] = None,
        key_3: typing.Optional[typing.Any] = None,
        key_4: typing.Optional[typing.Any] = None,
        key_5: typing.Optional[typing.Any] = None,
        key_6: typing.Optional[typing.Any] = None,
        key_7: typing.Optional[typing.Any] = None,
        key_8: typing.Optional[typing.Any] = None,
        key_9: typing.Optional[typing.Any] = None,
        key_up: typing.Optional[typing.Any] = None,
        key_down: typing.Optional[typing.Any] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class HotkeysPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    key_a: typing.Optional[typing.Any]
    key_b: typing.Optional[typing.Any]
    key_c: typing.Optional[typing.Any]
    key_d: typing.Optional[typing.Any]
    key_e: typing.Optional[typing.Any]
    key_f: typing.Optional[typing.Any]
    key_g: typing.Optional[typing.Any]
    key_h: typing.Optional[typing.Any]
    key_i: typing.Optional[typing.Any]
    key_j: typing.Optional[typing.Any]
    key_k: typing.Optional[typing.Any]
    key_l: typing.Optional[typing.Any]
    key_m: typing.Optional[typing.Any]
    key_n: typing.Optional[typing.Any]
    key_o: typing.Optional[typing.Any]
    key_p: typing.Optional[typing.Any]
    key_q: typing.Optional[typing.Any]
    key_r: typing.Optional[typing.Any]
    key_s: typing.Optional[typing.Any]
    key_t: typing.Optional[typing.Any]
    key_u: typing.Optional[typing.Any]
    key_v: typing.Optional[typing.Any]
    key_w: typing.Optional[typing.Any]
    key_x: typing.Optional[typing.Any]
    key_y: typing.Optional[typing.Any]
    key_z: typing.Optional[typing.Any]
    key_0: typing.Optional[typing.Any]
    key_1: typing.Optional[typing.Any]
    key_2: typing.Optional[typing.Any]
    key_3: typing.Optional[typing.Any]
    key_4: typing.Optional[typing.Any]
    key_5: typing.Optional[typing.Any]
    key_6: typing.Optional[typing.Any]
    key_7: typing.Optional[typing.Any]
    key_8: typing.Optional[typing.Any]
    key_9: typing.Optional[typing.Any]
    key_up: typing.Optional[typing.Any]
    key_down: typing.Optional[typing.Any]


class TriggerPluginV1(BasePluginV1):
    """Use this to configure triggers that trigger a specific action when an event occurs.

    The action is set in the action property, and the event is described in the other fields.

    The event can be triggered immediately when the task is loaded ("fireImmediately": true) or when data changes in
    the property specified in onChangeOf.

    You can also set conditions in the conditions property that must be met in order for the trigger to fire.
    Attributes:
        action: The action to perform when the trigger fires.
        condition: The condition that must be met in order to fire the trigger.
        fire_immediately: Flag indicating whether the trigger should be fired immediately after the task is loaded.
        on_change_of: The data that triggers the action when changed.

    Example:
        How to save Toloker's coordinates to the output.

        >>> coordinates_save_plugin = tb.plugins.TriggerPluginV1(
        >>>     fire_immediately=True,
        >>>     action=tb.actions.SetActionV1(
        >>>         data=tb.data.OutputData(path='performer_coordinates'),
        >>>         payload=tb.data.LocationData()
        >>>     ),
        >>> )
        ...
    """

    def __init__(
        self,
        *,
        action: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        condition: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        fire_immediately: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        on_change_of: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TriggerPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    action: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    condition: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    fire_immediately: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    on_change_of: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]


class TolokaPluginV1(BasePluginV1):
    """A plugin with extra settings for tasks in Toloka.

    Attributes:
        layout: Settings for the task appearance in Toloka.
        notifications: Notifications shown at the top of the page.

    Example:
        How to set the task width on the task page.

        >>> task_width_plugin = tb.plugins.TolokaPluginV1(
        >>>     'scroll',
        >>>     task_width=400,
        >>> )
        ...
    """

    class TolokaPluginLayout(toloka.client.project.template_builder.base.BaseTemplate):
        """How to display task.
        """

        class Kind(toloka.util._extendable_enum.ExtendableStrEnum):
            """An enumeration.

            Attributes:
                SCROLL: (default) display multiple tasks on the page at the same time.
                PAGER: display only one task on the page, with a button to switch between tasks at the bottom.
            """

            PAGER = 'pager'
            SCROLL = 'scroll'

        def __init__(
            self,
            kind: typing.Optional[Kind] = None,
            *,
            task_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None
        ) -> None:
            """Method generated by attrs for class TolokaPluginV1.TolokaPluginLayout.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        kind: typing.Optional[Kind]
        task_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]

    @typing.overload
    def __init__(
        self,
        layout: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, TolokaPluginLayout]] = ...,
        *,
        notifications: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[toloka.client.project.template_builder.base.BaseComponent]]] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TolokaPluginV1.
        """
        ...

    @typing.overload
    def __init__(
        self,
        kind: typing.Optional[TolokaPluginLayout.Kind] = None,
        *,
        task_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        notifications: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[toloka.client.project.template_builder.base.BaseComponent]]] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TolokaPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    layout: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, TolokaPluginLayout]]
    notifications: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[toloka.client.project.template_builder.base.BaseComponent]]]
