from .utils import read_toml
from .exceptions import InvalidProfileConfiguration, NoProfileFound
from .models import Profile
from .logging import logger

import os
import asyncio


class Vital:
    def __init__(self, profiles: str | list[str] = None):
        """ """

        # Load via profiles/ directory if no list of files are provided
        if not profiles:
            profiles = []

            current_dir = os.getcwd()
            parent_dir = os.path.dirname(current_dir)
            profiles_dir = os.path.join(parent_dir, "profiles")

            files = os.listdir(profiles_dir)

            for item in files:
                if item.endswith(".toml"):
                    profiles.append(f"{profiles_dir}/{item}")

        if not profiles:
            raise NoProfileFound("Could not find any profiles to load.")

        self.profiles: dict = {}

        for profile in profiles:
            try:
                data = read_toml(profile)
                name = profile.split("/")[-1].replace(".toml", "")
                print(f"Loading profile {name}...")
                # logger.info(f"Loading profile {name}...")

                if not data.get("profile"):
                    raise KeyError(
                        f"The profile object was not found in the {name} configuration file!"
                    )
                profile_dict = data["profile"]
                if profile_dict["enabled"]:
                    self.profiles[name] = Profile.model_validate(profile_dict)

            except Exception as ex:
                raise InvalidProfileConfiguration(
                    f"Your profile file could not be read!, Err: {ex}"
                )

    def start(self):
        """Start the vital engine"""
        asyncio.run(self.astart())

    async def astart(self):
        """Asynchronous start of the Vital engine"""
        self.active: bool = True
        try:
            while self.active:
                await asyncio.sleep(5)
        except (KeyboardInterrupt, asyncio.CancelledError):
            print("")
            logger.info(
                "shutdown",
                details="Graceful shutdown is starting...",
                trigger="keyboard_interrupt",
            )
        except Exception as ex:
            logger.error(
                "shutdown",
                exc_info=True,
                details="An exception caused a shutdown.",
                trigger=type(ex),
            )
        finally:
            self.active = False
            logger.info("shutdown", details="Shutdown is complete.")

    @staticmethod
    def dettached_monitor(self): ...

    @staticmethod
    def analytics(name: str, **kwargs):
        """Start analytics service. Give the service a name."""
