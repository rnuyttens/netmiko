"""Subclass specific to Cisco FTD."""
from typing import Any
import re
from netmiko.no_enable import NoEnable
from netmiko.no_config import NoConfig
from netmiko.cisco_base_connection import CiscoSSHConnection


class CiscoFtdSSH(NoEnable, NoConfig, CiscoSSHConnection):
    """Subclass specific to Cisco FTD."""

    def session_preparation(self) -> None:
        """Prepare the session after the connection has been established."""
        # Make sure the ASA is ready
        command = "show curpriv\n"
        self.write_channel(command)
        #self.read_until_pattern(pattern=re.escape(command.strip()))

        # The 'enable' call requires the base_prompt to be set.
        self.set_base_prompt()

    def send_config_set(self, *args: Any, **kwargs: Any) -> str:
        """Canot change config on FTD via ssh"""
        raise NotImplementedError

    def check_config_mode(
        self, check_string: str = "", pattern: str = "", force_regex: bool = False
    ) -> bool:
        """Canot change config on FTD via ssh"""
        return False
