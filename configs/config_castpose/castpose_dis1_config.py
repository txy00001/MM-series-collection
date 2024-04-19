_base_ = [
    '/home/txy/code/TXY_code/third_part/mmpose/configs/wholebody_2d_keypoint/rtmpose/ubody/rtmpose-l_8xb32-270e_coco-ubody-wholebody-384x288.py'  # noqa: E501
]

# model settings
find_unused_parameters = False

# config settings
fea = True
logit = True

# method details
model = dict(
    _delete_=True,
    type='DWPoseDistiller',
    teacher_pretrained='https://download.openmmlab.com/mmpose/v1/projects/'
    'rtmposev1/rtmpose-x_ucoco_384x288-f5b50679_20230822.pth',  # noqa: E501
    teacher_cfg='configs/wholebody_2d_keypoint/rtmpose/ubody/'
    'rtmpose-x_8xb32-270e_coco-ubody-wholebody-384x288.py',  # noqa: E501
    student_cfg='configs/wholebody_2d_keypoint/rtmpose/ubody/'
    'rtmpose-l_8xb32-270e_coco-ubody-wholebody-384x288.py',  # noqa: E501
    distill_cfg=[
        dict(methods=[
            dict(
                type='FeaLoss',
                name='loss_fea',
                use_this=fea,
                student_channels=1024,
                teacher_channels=1280,
                alpha_fea=0.00007,
            )
        ]),
        dict(methods=[
            dict(
                type='KDLoss',
                name='loss_logit',
                use_this=logit,
                weight=0.1,
            )
        ]),
    ],
    data_preprocessor=dict(
        type='PoseDataPreprocessor',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        bgr_to_rgb=True),
)
optim_wrapper = dict(clip_grad=dict(max_norm=1., norm_type=2))