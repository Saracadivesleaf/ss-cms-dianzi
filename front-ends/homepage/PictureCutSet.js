// JavaScript Document
(function(){
	var focusScroll_01 = new ScrollPic();
	focusScroll_01.scrollContId   = "scroll_jdt"; //内容容器ID
	focusScroll_01.dotListId = "slide_dot";
	focusScroll_01.dotClassName = "";
	focusScroll_01.dotOnClassName = "on";
	focusScroll_01.listType       = "";//列表类型(number:数字，其它为空)
	focusScroll_01.listEvent      = "onmouseover"; //切换事件
	focusScroll_01.frameWidth     = 1178;//显示框宽度
	focusScroll_01.pageWidth      = 1178; //翻页宽度
	focusScroll_01.upright        = false; //垂直滚动
	focusScroll_01.speed          = 10; //移动速度(单位毫秒，越小越快)
	focusScroll_01.space          = 60; //每次移动像素(单位px，越大越快)
	focusScroll_01.autoPlay       = true; //自动播放
	focusScroll_01.autoPlayTime   = 3; //自动播放间隔时间(秒)
	focusScroll_01.circularly     = true;
	focusScroll_01.initialize(); //初始化
	document.getElementById('scroll_left').onmousedown = function(){
		focusScroll_01.pre();
		return false;
	}
	document.getElementById('scroll_right').onmousedown = function(){
		focusScroll_01.next();
		return false;
	}
})()