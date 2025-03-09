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
#ifdef OLED_ENABLE
bool oled_task_user(void) {
    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
        case 0:
            oled_write_P(PSTR("Default\n"), false);
            break;
        case 1:
            oled_write_P(PSTR("FN\n"), false);
            break;
        case 2:
            oled_write_P(PSTR("ADJ\n"), false);
            break;
        default:
            // Or use the write_ln shortcut over adding '\n' to the end of your string
            oled_write_ln_P(PSTR("Undefined"), false);
    }


    return false;
}
#endif
