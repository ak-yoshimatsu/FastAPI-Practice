from fastapi import APIRouter
from returns.pipeline import flow, is_successful
from returns.result import Failure, Result, Success

router = APIRouter()


def get_paramter_value(value: str | None) -> Result[str, None]:
    if value is None:
        return Failure(value)
    return Success(value)


@router.get("/")
def index(q: str | None = None):
    print(f"param is {q}")
    # result = get_paramter_value(q)

    assert flow(get_paramter_value(q)) == Success()
    # if is_successful(result):
    #     print(result)
    #     return result.unwrap()
    # else:
    #     return result.failure().args
