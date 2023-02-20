!function(){
    var parameters = PluginManager.parameters('PatchVersionChecker');
    var targets = parameters['targets'];

    var create = Scene_Boot.prototype.create;
    Scene_Boot.prototype.create = function() {
        create.call(this);
        for (var target of targets) {
            check(target);
        }
    }

    var check = function(target) {
        var bool = true;
        if (target.startsWith('!')) {
            bool = false;
            target = target.substring(1);
        }
        var p = ImageManager.loadPicture(target);
        var i = setInterval(() => {
            if (p.isReady() || p.isError()) {
                if ((p.width == 1) == bool) {
                    alert('汉化补丁与游戏版本不一致，请重新下载。');
                    window.close();
                } else {
                    clearInterval(i);
                }
            }
        }, 0);
    }
}();