class IUoW:
    async def commit(self):
        raise NotImplementedError

    async def rollback(self):
        raise NotImplementedError

    async def flush(self):
        raise NotImplementedError
