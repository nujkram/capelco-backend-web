USERNAME_REGEX = "^[a-zA-Z0-9.-]*$"

SUPERADMIN = 'SU'
ADMIN = 'ADM'
USER = 'USR'

USER_TYPE_CHOICES = (
    (SUPERADMIN, 'Super Admin'),
    (ADMIN, 'Admin'),
    (USER, 'User'),
)


USER_DASHBOARD_ROOTS = {
    SUPERADMIN: 'MlxOaoMBHqgf',
    ADMIN: 'dashboard/admin',
    USER: '',
}