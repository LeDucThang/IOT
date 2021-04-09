from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from Repositories.UOW import UOW
router = InferringRouter()

@cbv(router)
class CategoryController:
    def __init__(self):
        self.UOW = UOW()

    route_item = "/items/abcdef" 
    @router.get(route_item)
    async def read_items(self):
        Categories = self.UOW.CategoryRepository.List()
        return Categories