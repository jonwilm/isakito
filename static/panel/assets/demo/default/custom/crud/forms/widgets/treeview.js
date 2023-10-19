var Treeview = function () {

    var demo = function () {
        $('.m_treeview_').jstree({
            "core" : {
                "themes" : {
                    "responsive": true
                }            
            },
            "types" : {
                "default" : {
                    "icon" : "fa fa-folder m--font-warning"
                },
                "file" : {
                    "icon" : "fa fa-file  m--font-warning"
                }
            },
            "plugins": ["types"]
        });
    }

    return {
        init: function () {
            demo();
        }
    };
}();

jQuery(document).ready(function() {    
    Treeview.init();
});