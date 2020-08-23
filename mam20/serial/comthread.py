from threading import Thread
from typing import Optional, Callable, Any, Iterable, Mapping


class CommunicationThread(Thread):

    def __init__(self, serial_io_port: str, group: None = ..., target: Optional[Callable[..., Any]] = ...,
                 name: Optional[str] = ...,
                 args: Iterable[Any] = ..., kwargs: Mapping[str, Any] = ..., *, daemon: Optional[bool] = ...) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.serial_io_port = serial_io_port
