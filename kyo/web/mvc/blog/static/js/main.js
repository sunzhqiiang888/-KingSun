$(document).ready(function(){
    console.log($("#prev_tool").height());
    console.log($("body").height() / 10);
    var top = ($("body").height() / 10 + 300) / 2;
    console.log(top);
    $("#prev_tool").css("top", top +"px");
    $("#next_tool").css("top", top +"px");

    $(".right_tool_list").click(function(){
        if ($("#right_list").hasClass("hide"))
            $("#right_list").addClass("show");
        if ($("#header").hasClass("slideUp"))
            $("#right_list").css("top", "0");
        else
            $("#right_list").css("top", "50px");
        $("#right_list").toggleClass("slideRight");
        $("#right_list").toggleClass("slideLeft");
    });
    $("#rtop").click(function(){
      window.scrollTo(0, 0);
    });
    $(document).popover({
      'content': '<img src="/blog/static/brcode.png" style="width:120px; height:120px;">',
      'html': true,
      'selector': '.barcode',
      'trigger': 'hover',
      'placement': 'left',
    });
});
var elem = document.getElementById("header");
var headroom = new Headroom(elem, {
  "tolerance": 5,
  "offset": 205,
  "classes": {
    "initial": "animated",
    "pinned": "slideDown",
    "unpinned": "slideUp"
  }
});
headroom.init();

