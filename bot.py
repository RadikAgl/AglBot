import sc2


class AglBot(sc2.BotAI):
    async def on_before_start(self):
        """
        Вызывается перед стартом.
        """
        pass

    async def on_start(self):
        """
        Вызывается единственный раз перед запуском on_step.
        """
        pass
        

    async def on_step(self, iteration):
        """
        Вызывается на каждом шаге игры.
        :param iteration:
        # """
        pass

    async def on_end(self, game_result):
        """
        Вызывается в конце игры.
        Обратить внимание запускается laddermanager
        """
        pass

    async def on_unit_destroyed(self, unit_tag):
        """
        Юнит уничтожен.
        """
        pass

    async def on_unit_created(self, unit):
        """ 
        Юнит создан
        """
        pass

    async def on_unit_type_changed(self, unit, previous_type):
        """ 
        Юнит изменил свой тип
        """
        pass

    async def on_building_construction_started(self, unit):
        """
        Начата постройка.
        """
        pass

    async def on_building_construction_complete(self, unit):
        """
        Постройка завершена.
        """
        pass

    async def on_upgrade_complete(self, upgrade):
        """
        Улучшение завершено.
        """
        pass

    async def on_unit_took_damage(self, unit, amount_damage_taken):
        """
        Юнит получил урон.
        """
        pass

    async def on_enemy_unit_entered_vision(self, unit):
        """
        Увидел врага.
        """
        pass

    async def on_enemy_unit_left_vision(self, unit_tag):
        """
        Вражеский юнит покинул зону видимости.
        """
        pass
