<!--
	@component
	Generates an SVG scatter plot. This component can also work if the x- or y-scale is ordinal, i.e. it has a `.bandwidth` method. See the [timeplot chart](https://layercake.graphics/example/Timeplot) for an example.
 -->
 <script>
	import { getContext } from 'svelte';
	import { scaleCanvas } from 'layercake';
	import { geoPath } from 'd3-geo';
	import {
		lonlat2xyz,
		euler2quat,
		quaternion,
		quatMultiply,
		quat2euler
	} from '$lib/rotation';

	const { zScale, width, height } = getContext('LayerCake');
	const { ctx } = getContext('canvas');

	export let extent;
	export let projection;
	// export let rotated_coords = { latitude: (Number = 0.0), longitude: (Number = 0.0) };
	export let rotate = [0, 0, 0];
	export let alpha = 0.5;
	export let grid = undefined;
	export let data = undefined;
	export let needsReset = true;

	let lat0;
	let lat1;
	let lon0;
	let lon1;
	let rotated_pole = [1, 0, 0, 0];

	$: {
		if (grid) {
			const longitude_shift = quaternion(
				lonlat2xyz([180 - grid.grid_north_pole_longitude, 0]),
				lonlat2xyz([0, 0])
			);
			const latitude_shift = quaternion(
				lonlat2xyz([0, grid.grid_north_pole_latitude]),
				lonlat2xyz([0, 90])
			);
			rotated_pole = quatMultiply(longitude_shift, latitude_shift);
		} else {
			rotated_pole = [1, 0, 0, 0]
		}
	}
	$: base_rotation = euler2quat(rotate);
	$: rotation = quat2euler(
		quatMultiply(base_rotation, quatMultiply(rotated_pole, euler2quat(projection().rotate())))
	);
	$: projectionFn = projection().rotate(rotation).fitSize([$width, $height], extent);
	$: geoPathFn = geoPath(projectionFn);

	$: {
		if ($ctx && geoPathFn && data) {
			/* --------------------------------------------
			 * If you were to have multiple canvas layers
			 * maybe for some artistic layering purposes
			 * put these reset functions in the first layer, not each one
			 * since they should only run once per update
			 */
			if (needsReset) {
				scaleCanvas($ctx, $width, $height);
				$ctx.clearRect(0, 0, $width, $height);
			}
			/* --------------------------------------------
			 * Draw our scatterplot
			 */
			// $ctx.imageSmoothingEnabled = true;
			// $ctx.globalCompositeOperation = "lighter"
			// $ctx.globalAlpha = alpha;
			if (data.latitude) {
				for (let latidx = 0; latidx < data.latitude.length; latidx++) {
					for (let lonidx = 0; lonidx < data.longitude.length; lonidx++) {
						// console.log(data.latitude[latidx], data.longitude[lonidx])
						lon0 = data.longitude[lonidx][0];
						lon1 = data.longitude[lonidx][1];
						lat0 = data.latitude[latidx][0];
						lat1 = data.latitude[latidx][1];
						$ctx.beginPath();
						geoPathFn.context($ctx);
						geoPathFn({
							type: 'Feature',
							geometry: {
								type: 'Polygon',
								coordinates: [
									[
										[lon0, lat0],
										[lon0, lat1],
										[lon1, lat1],
										[lon1, lat0],
										[lon0, lat0]
									]
								]
							}
						});
						$ctx.fillStyle = $zScale(data.value[latidx][lonidx]);
						$ctx.fill();
					}
				}
			} else {
				for (let ds of data.data) {
					$ctx.beginPath();
					geoPathFn.context($ctx);
					geoPathFn({
						type: 'Feature',
						geometry: {
							type: 'Polygon',
							coordinates: [
								[
									[ds.longitude[0], ds.latitude[0]],
									[ds.longitude[1], ds.latitude[1]],
									[ds.longitude[2], ds.latitude[2]],
									[ds.longitude[3], ds.latitude[3]],
									[ds.longitude[0], ds.latitude[0]]
								]
							]
						}
					});
					$ctx.fillStyle = $zScale(ds.value);
					$ctx.fill();
				}
			}
		}
	}
</script>
