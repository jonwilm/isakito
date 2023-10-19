//== Class definition

var BootstrapTimepicker = function () {
    
    function changeValue(input,value){
        /*
        var nativeInputValueSetter = Object.getOwnPropertyDescriptor(
          window.HTMLInputElement.prototype,
          "value"
        ).set;
        nativeInputValueSetter.call(input, value);
    
        var inputEvent = new Event("change", { bubbles: true });
        input.dispatchEvent(inputEvent);*/
        const event = new Event('change', { bubbles: true })
        input.value = value
        event.simulated = true;
        let tracker = input._valueTracker;
        if (tracker) {
            tracker.setValue(value);
        }
        input.dispatchEvent(event)
    }

    function setReactValue(element, value) {
        let lastValue = element.value;
        element.value = value;
        let event = createNewEvent("input", element);
        event.simulated = true;
        let tracker = element._valueTracker;
        if (tracker) {
          tracker.setValue(lastValue);
          element.dispatchEvent(event);
        }
        return lastValue;
      }
      
      function createNewEvent(eventName, element) {
          let event;
          if (typeof(Event) === 'function') {
              event = new Event(eventName, {target: element, bubbles:true});
          } else {
              event = document.createEvent('Event');
              event.initEvent(eventName, true, true);
              element.addEventListener(eventName, function(e) {
                e.target = element;
              });
          }
          return event;
      }

    //== Private functions
    var demos = function () {
        $('.m_timepicker_').timepicker({
            defaultTime: '',
            minuteStep: 1
        }).on('hide.timepicker', function(e) {
            const input = document.getElementsByName(e.target.name)[0];
            //console.log(document.querySelector(`[name=${e.target.name}]`));
            const value = e.time.value;
            //console.log(e);
            //console.log(input);
            //console.log(value);
            changeValue(input,value);
            //setReactValue(input,value);
            
        });
    }

    return {
        // public functions
        init: function() {
            demos(); 
        }
    };
}();