var BootstrapDatetimepicker = function () {
    var arrows;
    if (mUtil.isRTL()) {
        arrows = {
            leftArrow: '<i class="la la-angle-right"></i>',
            rightArrow: '<i class="la la-angle-left"></i>'
        }
    } else {
        arrows = {
            leftArrow: '<i class="la la-angle-left"></i>',
            rightArrow: '<i class="la la-angle-right"></i>'
        }
    }

    var demos = function () {
        $.fn.datetimepicker.dates['es'] = {
            days: ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"],
            daysShort: ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"],
            daysMin: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"],
            months: [ "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" ],
            monthsShort: [ "Ene", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic" ],
            today: "Hoy",
            clear: "Limpiar Fecha",
            weekStart: 1
        };

        $('.m_datetimepicker_').datetimepicker({
            rtl: mUtil.isRTL(),
            todayHighlight: true,
            clearBtn:true,
            format: 'dd/mm/yyyy hh:ii',
            language:"es"
        });
    }

    return {
        init: function() {
            demos(); 
        }
    };
}();