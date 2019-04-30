class Monster {
    constructor(options={}) {
        this.health = 100;
        this.name = options.name;
    }
}

class Spider extends Monster {
    constructor(options) {
        super(options)
    }
    static bite (monster) {
        monster.health -= 10;
    }
}

spidy = new Spider({ name: '거미인간'});
mob = new Monster({ name: '미니언'});
Spider.bite(mob);
console.log(spidy.name, spidy.health); // 거미인간 100
console.log(mob.name, mob.health); // 미니언 90