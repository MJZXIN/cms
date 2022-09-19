from utils.database import db, TblCorp, TblDept, TblPost, TblUser, TblRole, TblPart, TblWhsh
from utils.jwtimpl import JwtImpl, SALT
from utils.result import Result
from utils.decorators import has_role, has_roles
