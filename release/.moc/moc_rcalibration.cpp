/****************************************************************************
** Meta object code from reading C++ file 'rcalibration.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../include/rcalibration.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'rcalibration.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_rcalibration[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      13,   52,   53,   52, 0x0a,
      58,   52,   53,   52, 0x0a,
      82,  107,   52,   52, 0x09,
     113,  132,   52,   52, 0x09,
     138,  132,   52,   52, 0x09,
     160,  184,   52,   52, 0x09,
     188,  184,   52,   52, 0x09,
     214,  184,   52,   52, 0x09,
     240,  184,   52,   52, 0x09,
     268,   52,   52,   52, 0x09,
     305,   52,   52,   52, 0x09,

       0        // eod
};

static const char qt_meta_stringdata_rcalibration[] = {
    "rcalibration\0onStartReticleCalibrationButtonClick()\0"
    "\0bool\0onFindStarButtonClick()\0"
    "onSquareSizeChanged(int)\0index\0"
    "onTwoAxisMode(int)\0state\0onEnableAutoMode(int)\0"
    "onDriftTimeChanged(int)\0val\0"
    "onReticleXChanged(double)\0"
    "onReticleYChanged(double)\0"
    "onReticleAngChanged(double)\0"
    "onStartVideoCalibrationButtonClick()\0"
    "onVideoCalibrationFinished()\0"
};

void rcalibration::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        rcalibration *_t = static_cast<rcalibration *>(_o);
        switch (_id) {
        case 0: { bool _r = _t->onStartReticleCalibrationButtonClick();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = _r; }  break;
        case 1: { bool _r = _t->onFindStarButtonClick();
            if (_a[0]) *reinterpret_cast< bool*>(_a[0]) = _r; }  break;
        case 2: _t->onSquareSizeChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 3: _t->onTwoAxisMode((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->onEnableAutoMode((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 5: _t->onDriftTimeChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->onReticleXChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 7: _t->onReticleYChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 8: _t->onReticleAngChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 9: _t->onStartVideoCalibrationButtonClick(); break;
        case 10: _t->onVideoCalibrationFinished(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData rcalibration::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject rcalibration::staticMetaObject = {
    { &QDialog::staticMetaObject, qt_meta_stringdata_rcalibration,
      qt_meta_data_rcalibration, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &rcalibration::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *rcalibration::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *rcalibration::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_rcalibration))
        return static_cast<void*>(const_cast< rcalibration*>(this));
    return QDialog::qt_metacast(_clname);
}

int rcalibration::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 11)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 11;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
