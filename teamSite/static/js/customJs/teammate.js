$(function() { 
	var _index5=0;

	//点击右边按钮
	$("#four_flash .but_right img").click(function(){
		_index5++;
		var len=$(".flashBg ul.mobile li").length;
		// 每行摆3个,大于len了就要重新循环,所以要加上
		if(_index5+3>len){
			$("#four_flash .flashBg ul.mobile").stop().append($("ul.mobile").html());
		}
		//270为一个li的宽度
		$("#four_flash .flashBg ul.mobile").stop().animate({left:-_index5*270},1000);
	});

	//点击左边按钮
	$("#four_flash .but_left img").click(function(){
		if(_index5==0){
			$("ul.mobile").prepend($("ul.mobile").html());
			// 天知道这个1890是怎么算出来的。。
			$("ul.mobile").css("left","-1890px");
			_index5=7;
		}
		_index5--;
		$("#four_flash .flashBg ul.mobile").stop().animate({left:-_index5*270},1000);
	});

	//点击了解更多
	$("#maininfo a").click(function(){
		// 以index的路径为基本路径 http://127.0.0.1:8000/index/teaminfo
		window.location.href="teaminfo";
	});

});
