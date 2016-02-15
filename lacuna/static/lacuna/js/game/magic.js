function magicinit() {
    function a() {
        for (var a = "", i = 0; 7 > i; i++)
            for (var d = i; 7 > d; d++) a += '<div class="dice_cont"> <div class="top_val" data-val="' + i + '">' + i + '</div> <div class="bottom_val" data-val="' + d + '">' + d + "</div> </div>";
        $("#dice_wrapper").html(a), $(".dice_cont").draggable(o), $(".drop_dice").droppable({
            drop: function(a, i) {
                var d = $(this);
                return d.find(".dice_cont").length >= 1 ? void i.draggable.draggable("option", "revert", !0) : (i.draggable.appendTo(d).css({
                    top: "0px",
                    left: "0px"
                }), void t())
            }
        }), $(".dice_cont").click(function() {
            var a = $(this).find(".top_val"),
                t = $(this).find(".bottom_val"),
                i = t.data("val");
            t.data("val", a.data("val")), t.text(a.data("val")), a.data("val", i), a.text(i)
        }), $("#place_dice").on("click", ".dice_cont", function() {
            t()
        })
    }

    function t() {
        var a = !0,
            t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        $(".drop_dice").each(function() {
            var t = $(this).find(".dice_cont");
            0 != t.length ? (i[$(this).data("i")][$(this).data("j")] = t.find(".top_val").data("val"), i[$(this).data("i") + 1][$(this).data("j")] = t.find(".bottom_val").data("val")) : (a = !1, i[$(this).data("i")][$(this).data("j")] = 0, i[$(this).data("i") + 1][$(this).data("j")] = 0)
        });
        for (var o = 0; o < i.length; o++) {
            for (var n = 0; n < i[o].length; n++) t[o + 6] += i[o][n], t[n + 1] += i[o][n];
            t[0] += i[o][o], t[5] += i[o][3 - o]
        }
        for (var o = 0; o < t.length; o++) $("#sum" + (o + 1)).html(t[o]), t[o] != d && (a = !1);
        a && submit_ans(i, 7)
    }
    var i = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        d = 6,
        o = {
            revert: "invalid",
            stop: function() {
                $(this).draggable("option", "revert", "invalid")
            }
        };
    a(), $("#dice_wrapper").droppable({
        drop: function(a, i) {
            var d = $(this);
            i.draggable.appendTo(d).css({
                top: "0px",
                left: "0px"
            }), t()
        }
    })
}