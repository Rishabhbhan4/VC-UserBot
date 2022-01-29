from pyrogram import (
    filters
)
from config import (
    SUDO_USERS
)
from EvaMaria.darkprince.admincheck import admin_check


def f_sudo_filter(filt, client, message):
    return bool(
        message.from_user.id in SUDO_USERS
    )


sudo_filter = filters.create(
    func=f_sudo_filter,
    name="SudoFilter"
)


def onw_filter(filt, client, message):
    if SUDO_USERS:
        return bool(
            True # message.from_user.id in SUDO_USERS
        )
    else:
        return bool(
            message.from_user and
            message.from_user.is_self
        )


f_onw_fliter = filters.create(
    func=onw_filter,
    name="OnwFilter"
)


async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)
