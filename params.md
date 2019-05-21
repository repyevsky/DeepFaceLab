# Params

## Convertor

mode -- "Choose mode: (1) overlay, (2) hist match, (3) hist match bw, (4) seamless, (5) raw."

raw_mode_variation -- "Choose raw mode: (1) rgb, (2) rgb+mask (default), (3) mask only, (4) predicted only : "

hist_match_threshold -- "Hist match threshold [0..255] (skip:255)

mask -- `"Mask mode: (1) learned, (2) dst, (3) FAN-prd, (4) FAN-dst , (5) FAN-prd*FAN-dst (6) learned*FAN-prd*FAN-dst (?) help. Default - %d : " % (1) , 1, help_message="If you learned mask, then option 1 should be choosed. 'dst' mask is raw shaky mask from dst aligned images. 'FAN-prd' - using super smooth mask by pretrained FAN-model from predicted face. 'FAN-dst' - using super smooth mask by pretrained FAN-model from dst face. 'FAN-prd*FAN-dst' or 'learned*FAN-prd*FAN-dst' - using multiplied masks."`

erode_mask -- "Choose erode mask modifier [-200..200] (skip:%d) : "

blur_mask -- "Choose blur mask modifier [-200..200] (skip:%d) : "

output_scale -- "Choose output face scale modifier [-50..50] (skip:0) : "

color -- "Apply color transfer to predicted face? Choose mode ( rct/lct skip:None ) : "

degrade_color -- "Degrade color power of final image [0..100] (skip:0) : "

export_png -- "Export png with alpha channel? (y/n skip:n) : "