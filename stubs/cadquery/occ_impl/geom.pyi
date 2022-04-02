from OCP.Bnd import Bnd_Box
from OCP.TopLoc import TopLoc_Location
from OCP.TopoDS import TopoDS_Shape as TopoDS_Shape
from OCP.gp import gp_Ax3, gp_Dir, gp_GTrsf, gp_Pln, gp_Pnt, gp_Trsf, gp_Vec, gp_XYZ
from typing import Any, Optional, Sequence, Tuple, Union, overload

TOL: float

class Vector:
    @overload
    def __init__(self, x: float, y: float, z: float) -> None: ...
    @overload
    def __init__(self, x: float, y: float) -> None: ...
    @overload
    def __init__(self, v: Vector) -> None: ...
    @overload
    def __init__(self, v: Sequence[float]) -> None: ...
    @overload
    def __init__(self, v: Union[gp_Vec, gp_Pnt, gp_Dir, gp_XYZ]) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, value: float) -> None: ...
    @property
    def Length(self) -> float: ...
    @property
    def wrapped(self) -> gp_Vec: ...
    def toTuple(self) -> Tuple[float, float, float]: ...
    def cross(self, v: Vector) -> Vector: ...
    def dot(self, v: Vector) -> float: ...
    def sub(self, v: Vector) -> Vector: ...
    def __sub__(self, v: Vector) -> Vector: ...
    def add(self, v: Vector) -> Vector: ...
    def __add__(self, v: Vector) -> Vector: ...
    def multiply(self, scale: float) -> Vector: ...
    def __mul__(self, scale: float) -> Vector: ...
    def __truediv__(self, denom: float) -> Vector: ...
    def __rmul__(self, scale: float) -> Vector: ...
    def normalized(self) -> Vector: ...
    def Center(self) -> Vector: ...
    def getAngle(self, v: Vector) -> float: ...
    def getSignedAngle(self, v: Vector) -> float: ...
    def distanceToLine(self) -> None: ...
    def projectToLine(self, line: Vector) -> Vector: ...
    def distanceToPlane(self) -> None: ...
    def projectToPlane(self, plane: Plane) -> Vector: ...
    def __neg__(self) -> Vector: ...
    def __abs__(self) -> float: ...
    def __eq__(self, other: Vector) -> bool: ...
    def toPnt(self) -> gp_Pnt: ...
    def toDir(self) -> gp_Dir: ...
    def transform(self, T: Matrix) -> Vector: ...

class Matrix:
    wrapped: gp_GTrsf
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, matrix: Union[gp_GTrsf, gp_Trsf]) -> None: ...
    @overload
    def __init__(self, matrix: Sequence[Sequence[float]]) -> None: ...
    def rotateX(self, angle: float): ...
    def rotateY(self, angle: float): ...
    def rotateZ(self, angle: float): ...
    def inverse(self) -> Matrix: ...
    @overload
    def multiply(self, other: Vector) -> Vector: ...
    @overload
    def multiply(self, other: Matrix) -> Matrix: ...
    def transposed_list(self) -> Sequence[float]: ...
    def __getitem__(self, rc: Tuple[int, int]) -> float: ...

class Plane:
    xDir: Vector
    yDir: Vector
    zDir: Vector
    lcs: gp_Ax3
    rG: Matrix
    fG: Matrix
    @classmethod
    def named(cls, stdName: str, origin=...) -> Plane: ...
    @classmethod
    def XY(cls, origin=..., xDir=...): ...
    @classmethod
    def YZ(cls, origin=..., xDir=...): ...
    @classmethod
    def ZX(cls, origin=..., xDir=...): ...
    @classmethod
    def XZ(cls, origin=..., xDir=...): ...
    @classmethod
    def YX(cls, origin=..., xDir=...): ...
    @classmethod
    def ZY(cls, origin=..., xDir=...): ...
    @classmethod
    def front(cls, origin=..., xDir=...): ...
    @classmethod
    def back(cls, origin=..., xDir=...): ...
    @classmethod
    def left(cls, origin=..., xDir=...): ...
    @classmethod
    def right(cls, origin=..., xDir=...): ...
    @classmethod
    def top(cls, origin=..., xDir=...): ...
    @classmethod
    def bottom(cls, origin=..., xDir=...): ...
    def __init__(self, origin: Union[Tuple[float, float, float], Vector], xDir: Optional[Union[Tuple[float, float, float], Vector]] = ..., normal: Union[Tuple[float, float, float], Vector] = ...) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @property
    def origin(self) -> Vector: ...
    @origin.setter
    def origin(self, value) -> None: ...
    def setOrigin2d(self, x, y) -> None: ...
    def toLocalCoords(self, obj): ...
    def toWorldCoords(self, tuplePoint) -> Vector: ...
    def rotated(self, rotate=...): ...
    def mirrorInPlane(self, listOfShapes, axis: str = ...): ...
    @property
    def location(self) -> Location: ...
    def toPln(self) -> gp_Pln: ...

class BoundBox:
    wrapped: Bnd_Box
    xmin: float
    xmax: float
    xlen: float
    ymin: float
    ymax: float
    ylen: float
    zmin: float
    zmax: float
    zlen: float
    center: Any
    DiagonalLength: Any
    def __init__(self, bb: Bnd_Box) -> None: ...
    def add(self, obj: Union[Tuple[float, float, float], Vector, 'BoundBox'], tol: Optional[float] = ...) -> BoundBox: ...
    @staticmethod
    def findOutsideBox2D(bb1: BoundBox, bb2: BoundBox) -> Optional['BoundBox']: ...
    def isInside(self, b2: BoundBox) -> bool: ...

class Location:
    wrapped: TopLoc_Location
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, t: Vector) -> None: ...
    @overload
    def __init__(self, t: Plane) -> None: ...
    @overload
    def __init__(self, t: Plane, v: Vector) -> None: ...
    @overload
    def __init__(self, t: TopLoc_Location) -> None: ...
    @overload
    def __init__(self, t: gp_Trsf) -> None: ...
    @overload
    def __init__(self, t: Vector, ax: Vector, angle: float) -> None: ...
    @property
    def inverse(self) -> Location: ...
    def __mul__(self, other: Location) -> Location: ...
    def toTuple(self) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]: ...