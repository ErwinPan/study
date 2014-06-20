// JavaScript Document
function homeSlideShow() {
    if ($('.dynamicAd').has($('.slider')).length > 0) {
        $('.slider').nivoSlider();
    }
}
function addShadow() {
    if ($('.advanceRadioButtonList').length > 0) {
        $('.advanceRadioButtonList').animate({ boxShadow: '9px 9px 14px 0px  rgba(55,55,55, 0.3)' });
    }
}
function advanceSearchListHover() {
    //	if($('.advanceSearchList').length >0){
    //		$('.advanceSearchList').toggle(function(){$('.advanceRadioButtonList').show()},function(){$('.advanceRadioButtonList').hide()});
    //	}
}
function advanceRadioButtonListClosed() {
    if ($('.advanceRadioButtonList').length > 0) {
        $('.advanceRadioButtonList close').click(function () { $('.advanceRadioButtonList').hide() });
    }
}
function searchItemHover() {
    //    if ($('.searchItemList').length > 0) {
    //        $('.searchItemList li').hover(
    //    function () {
    //        $(this).prepend("<div class='searchItemListHoverBorder'></div>");
    //    },
    //    function () {
    //        $(this).find("div").remove();
    //    }
    //  );
    //    }
}
function lotNumberToggle() {
    if ($('.lotNumberBtn').length > 0) {
        $('.lotNumberBtn').toggle(function () { $('.lotNumberList').show() }, function () { $('.lotNumberList').hide(); });
    }
}
$(function () {
    homeSlideShow();

    addShadow();
    advanceSearchListHover();
    lotNumberToggle();
});