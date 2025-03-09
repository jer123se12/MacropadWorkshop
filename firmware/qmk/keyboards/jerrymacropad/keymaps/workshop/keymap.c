#include QMK_KEYBOARD_H

enum custom_keycodes {
   SPEEE = SAFE_RANGE,
};
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
  [0] = LAYOUT(
      LCTL(KC_C),LCTL(KC_V) ,SPEEE
   )
};

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode){
        case SPEEE:
            if (record->event.pressed){

               send_string_with_delay("https://sopossible.sp.edu.sg/courses/schools/eee",3);
               return false;
            }
            break;
    };
    return true;

};
layer_state_t layer_state_set_user(layer_state_t state) {
    switch (get_highest_layer(state)) {
    case 0:
        rgblight_setrgb (0x00,  0x00, 0x55);
        break;
    case 1:
        rgblight_setrgb (0x55,  0x00, 0x00);
        break;
    case 2:
        rgblight_setrgb (0x00,  0x55, 0x00);
        break;
    case 3:
        rgblight_setrgb (0x55,  0x00, 0x55);
        break;
    default: //  for any other layers, or the default layer
        rgblight_setrgb (0x55,  0x55, 0x55);
        break;
    }
  return state;
};
