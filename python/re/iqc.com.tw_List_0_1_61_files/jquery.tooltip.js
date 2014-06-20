$(document).ready(function(){
    if($('#_tooltip').attr('id') == null){
        $(document.createElement('div')).attr('id', '_tooltip').prependTo('body');
    }
});


;(function($){

    function setTooltip(o)
    {
        var oTooltip = $('#_tooltip');
            
        //oTooltip.width('');oTooltip.height('');
        oTooltip.html($(o).attr('tooltip'));
        var str = new String($(o).attr('tooltip'));            
        oTooltip.css('position', 'absolute');
        oTooltip.css('overflow', 'hidden');
        
//        if(oTooltip.width() > 360)
//            oTooltip.width('360px');
//        if(oTooltip.height() > 360)
//            oTooltip.height('360px');
        
        var cw = document.documentElement.clientWidth?document.documentElement.clientWidth:document.body.clientWidth?document.body.clientWidth:window.innerWidth?window.innerWidth:0;
        var ch = document.documentElement.clientHeight?document.documentElement.clientHeight:document.body.clientHeight?document.body.clientHeight:window.innerHeight?window.innerHeight:0;
        var ow = oTooltip.innerWidth();
        var oh = oTooltip.innerHeight();
        var st = $(document).scrollTop();
        var sl = $(document).scrollLeft();
        
        var offset = $(o).offset();
        var tx = offset.left;
        var ty = offset.top;
        var tw = $(o).width();   
        var th = $(o).height();
        
        var px = tx - ow < sl?tx + tw:tx - ow;
        var py = ty - oh < st?ty + th:ty - oh;
        
        oTooltip.css('left', px + 'px');
        oTooltip.css('top', py + 'px');
        oTooltip.css('background-color', '#FCF9C2');
        oTooltip.css('border', '1px solid #000');
        oTooltip.css('z-index', '99');
        oTooltip.click(function(){$(o).trigger('click');});
        oTooltip.show();
    }
    
    function hideTooltip()
    {
        $('#_tooltip').hide();
    }

    $.tooltip = { 
        get : function(){ return $('#_tooltip');},
        
        reload : function(){ this.bind();},
        
        hide : function(){ hideTooltip(); },
        
        bind : function(){
            $('[tooltip]').live('mouseover', function(e){
                setTooltip(this);
            });
            $('[tooltip]').live('mouseout', function(){
                hideTooltip();
            });
        },
        
        load : function(t){
            setTooltip(t);
        }
    }
})(jQuery);

$.tooltip.bind();